"""MLflow wiring: where runs are stored, how experiments are named, and how a
run is tied back to the exact code that produced it.

mlflow is imported inside the functions that use it, the same discipline the
package applies to torch: importing `smart_tagging.tracking` must stay cheap and
must not require the tracking stack to be present.
"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "CODE_REF_ENV",
    "UNKNOWN_CODE_REF",
    "CodeIdentity",
    "experiment_name",
    "resolve_code_identity",
    "start_run",
    "tracking_uri",
]

# Set by the cloud launcher, which knows the immutable reference it installed
# from. See resolve_code_ref.
CODE_REF_ENV = "SMART_TAGGING_CODE_REF"
UNKNOWN_CODE_REF = "unknown"


def tracking_uri(root: Path | None = None) -> str:
    """Local SQLite backend, no server involved.

    The backlog asked for a "file backend", meaning local rather than hosted.
    MLflow has since put the plain `./mlruns` file store into maintenance mode
    and refuses it without an explicit opt-out, so this uses SQLite instead: it
    keeps the intent — one local file, nothing to run — without starting the
    project on a deprecated path. `mlflow.db` is excluded from Git.
    """
    root = root or Path.cwd()
    return f"sqlite:///{(root / 'mlflow.db').resolve().as_posix()}"


@dataclass(frozen=True)
class CodeIdentity:
    """Which code ran, and whether that claim can be trusted.

    The two travel together on purpose. A commit SHA logged on its own
    overclaims: it names a commit while the process may be running edits that
    were never committed. Binding `dirty` to `ref` in one object means the
    caveat cannot be forgotten at the call site — the design prevents the
    defect instead of documenting it.
    """

    ref: str
    dirty: bool | None

    def as_tags(self) -> dict[str, str]:
        return {
            "code_ref": self.ref,
            "code_dirty": "unknown" if self.dirty is None else str(self.dirty),
        }


def _git(*args: str) -> str | None:
    """Run a Git command, or return None if Git cannot answer."""
    try:
        completed = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True
        )
    except (OSError, subprocess.CalledProcessError):
        # No git binary, or not inside a work tree.
        return None
    return completed.stdout


def resolve_code_identity() -> CodeIdentity:
    """Identify the code that is running.

    Locally this is the Git commit SHA, plus whether the working tree matches
    it. In a Kaggle session there is no `.git` at all — the package arrives
    installed, not cloned — so MLflow cannot find a commit to record and a run
    would otherwise be orphaned from its code.

    The launcher solves that by installing from an immutable reference and
    exporting the same reference here. The identifier is not so much
    transmitted as reused: it *is* what determined which code ran. There is no
    working tree in that case, so `dirty` is None rather than False — "not
    applicable" and "clean" are different facts.

    Returns UNKNOWN_CODE_REF when neither source is available, on purpose: a run
    that cannot be tied to its code should say so instead of looking like every
    other run.
    """
    declared = os.environ.get(CODE_REF_ENV)
    if declared:
        # Explicit wins: it is the deliberate answer for environments with no
        # Git metadata to infer from.
        return CodeIdentity(ref=declared, dirty=None)

    head = _git("rev-parse", "HEAD")
    if head is None or not head.strip():
        return CodeIdentity(ref=UNKNOWN_CODE_REF, dirty=None)

    # --porcelain lists modified, staged and untracked files alike. Untracked
    # counts here: with an editable install, an uncommitted .py under src/ is
    # imported like any other module.
    status = _git("status", "--porcelain")
    dirty = None if status is None else bool(status.strip())
    return CodeIdentity(ref=head.strip(), dirty=dirty)


def experiment_name(hypothesis: str, splits_version: str) -> str:
    """One experiment per hypothesis; each model is a run inside it.

    The comparison that matters is several models against the same question, so
    the hypothesis is the unit that groups runs. The splits version is part of
    the name because comparing runs computed over different frozen splits is not
    comparing (I2) — and if the name does not carry it, nothing stops you.
    """
    return f"{hypothesis}__splits-{splits_version}"


def start_run(
    hypothesis: str,
    splits_version: str,
    run_name: str,
    seed_tags: dict[str, str] | None = None,
    root: Path | None = None,
) -> Any:
    """Open an MLflow run already tagged with its identity.

    Returns MLflow's own run context manager, so callers use it with `with`.
    """
    import mlflow

    mlflow.set_tracking_uri(tracking_uri(root))
    mlflow.set_experiment(experiment_name(hypothesis, splits_version))

    run = mlflow.start_run(run_name=run_name)
    mlflow.set_tags({**resolve_code_identity().as_tags(), **(seed_tags or {})})
    return run
