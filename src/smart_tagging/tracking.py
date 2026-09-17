"""MLflow wiring: where runs are stored, how experiments are named, and how a
run is tied back to the exact code that produced it.

mlflow is imported inside the functions that use it, the same discipline the
package applies to torch: importing `smart_tagging.tracking` must stay cheap and
must not require the tracking stack to be present.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

__all__ = [
    "CODE_REF_ENV",
    "UNKNOWN_CODE_REF",
    "experiment_name",
    "resolve_code_ref",
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


def resolve_code_ref() -> str:
    """Identify the code that is running.

    Locally this is the Git commit SHA. In a Kaggle session there is no `.git`
    at all — the package arrives installed, not cloned — so MLflow cannot find
    a commit to record, and a run would otherwise be orphaned from its code.

    The launcher solves it by installing from an immutable reference and
    exporting that same reference here. The identifier is not transmitted so
    much as reused: it *is* the thing that determined which code ran.

    Returns UNKNOWN_CODE_REF when neither source is available. That value is
    logged as-is and on purpose: a run that cannot be tied to its code should
    say so in the record instead of looking like every other run.
    """
    declared = os.environ.get(CODE_REF_ENV)
    if declared:
        # Explicit wins: it is the deliberate answer for environments that have
        # no Git metadata to infer from.
        return declared

    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        # No git binary, or not inside a work tree.
        return UNKNOWN_CODE_REF
    return completed.stdout.strip() or UNKNOWN_CODE_REF


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
    mlflow.set_tags({"code_ref": resolve_code_ref(), **(seed_tags or {})})
    return run
