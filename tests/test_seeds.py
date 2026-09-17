"""Tests for deterministic seeding (F0.7)."""

import importlib.util
import random

import numpy as np

from smart_tagging.seeds import set_seeds


def test_same_seed_gives_the_same_draws():
    set_seeds(123)
    first = (random.random(), np.random.rand())

    set_seeds(123)
    second = (random.random(), np.random.rand())

    assert first == second


def test_different_seeds_give_different_draws():
    """Guards against the seeding silently doing nothing at all.

    Without this, a `set_seeds` that seeded no generator would still pass the
    test above — two identical no-ops produce identical results for the wrong
    reason.
    """
    set_seeds(123)
    first = (random.random(), np.random.rand())

    set_seeds(456)
    second = (random.random(), np.random.rand())

    assert first != second


def test_the_report_matches_what_is_actually_installed():
    """The report is the evidence behind the word "reproducible", so it has to
    describe this environment rather than an assumed one. Passes both in CI,
    where torch is absent, and locally with the `local` extra installed."""
    report = set_seeds(7)

    assert report.seed == 7
    assert report.python is True
    assert report.numpy is True
    assert report.torch is (importlib.util.find_spec("torch") is not None)


def test_tags_are_flat_strings():
    """Experiment trackers take string tags; a nested value would be silently
    stringified into something unreadable."""
    tags = set_seeds(7).as_tags()

    assert tags["seed.seed"] == "7"
    assert all(isinstance(v, str) for v in tags.values())
