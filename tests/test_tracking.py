"""Tests for run identity and experiment naming (F0.7).

None of these import mlflow: the point of keeping that import inside the
functions is that the module stays testable without the tracking stack.
"""

import re

from smart_tagging.tracking import (
    CODE_REF_ENV,
    UNKNOWN_CODE_REF,
    experiment_name,
    resolve_code_identity,
)


def test_an_explicit_code_ref_wins_over_git(monkeypatch):
    """The launcher's declared reference is the deliberate answer for
    environments with no Git metadata, so it must not be overridden by whatever
    repository the process happens to be standing in."""
    monkeypatch.setenv(CODE_REF_ENV, "deadbeef")

    identity = resolve_code_identity()

    assert identity.ref == "deadbeef"
    assert identity.dirty is None, "there is no working tree to call clean"


def test_a_run_with_no_identity_says_so(monkeypatch, tmp_path):
    """Outside a work tree and with nothing declared, the answer is the sentinel
    — not a plausible-looking blank. A run that cannot be tied to its code has
    to be visible as such in the record."""
    monkeypatch.delenv(CODE_REF_ENV, raising=False)
    monkeypatch.chdir(tmp_path)

    identity = resolve_code_identity()

    assert identity.ref == UNKNOWN_CODE_REF
    assert identity.dirty is None


def test_inside_this_repository_the_ref_is_a_sha_and_dirty_is_known(monkeypatch):
    """A commit SHA on its own overclaims: it names a commit while the process
    may be running edits that were never committed. Both facts or neither."""
    monkeypatch.delenv(CODE_REF_ENV, raising=False)

    identity = resolve_code_identity()

    assert re.fullmatch(r"[0-9a-f]{40}", identity.ref)
    assert isinstance(identity.dirty, bool)


def test_unknown_dirtiness_is_not_reported_as_clean():
    """ "Not applicable" and "clean" are different facts, and collapsing them
    would let a Kaggle run look as trustworthy as a verified local one."""
    from smart_tagging.tracking import CodeIdentity

    assert CodeIdentity("abc", None).as_tags()["code_dirty"] == "unknown"
    assert CodeIdentity("abc", False).as_tags()["code_dirty"] == "False"
    assert CodeIdentity("abc", True).as_tags()["code_dirty"] == "True"


def test_the_experiment_name_carries_the_splits_version():
    """Comparing runs computed over different frozen splits is not comparing
    (I2). The name is where that becomes visible instead of assumed."""
    name = experiment_name("H3b", "2026-09-17-a")

    assert "H3b" in name
    assert "2026-09-17-a" in name
