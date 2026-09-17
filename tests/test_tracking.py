"""Tests for run identity and experiment naming (F0.7).

None of these import mlflow: the point of keeping that import inside the
functions is that the module stays testable without the tracking stack.
"""

from smart_tagging.tracking import (
    CODE_REF_ENV,
    UNKNOWN_CODE_REF,
    experiment_name,
    resolve_code_ref,
)


def test_an_explicit_code_ref_wins_over_git(monkeypatch):
    """The launcher's declared reference is the deliberate answer for
    environments with no Git metadata, so it must not be overridden by whatever
    repository the process happens to be standing in."""
    monkeypatch.setenv(CODE_REF_ENV, "deadbeef")

    assert resolve_code_ref() == "deadbeef"


def test_a_run_with_no_identity_says_so(monkeypatch, tmp_path):
    """Outside a work tree and with nothing declared, the answer is the sentinel
    — not a plausible-looking blank. A run that cannot be tied to its code has
    to be visible as such in the record."""
    monkeypatch.delenv(CODE_REF_ENV, raising=False)
    monkeypatch.chdir(tmp_path)

    assert resolve_code_ref() == UNKNOWN_CODE_REF


def test_the_experiment_name_carries_the_splits_version():
    """Comparing runs computed over different frozen splits is not comparing
    (I2). The name is where that becomes visible instead of assumed."""
    name = experiment_name("H3b", "2026-09-17-a")

    assert "H3b" in name
    assert "2026-09-17-a" in name
