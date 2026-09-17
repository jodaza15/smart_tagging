"""Smoke tests for the package itself (F0.6).

These are the executable half of this task's "done when": they fail loudly if the
package is not really installed, or if the import graph starts depending on a
runtime that CI does not install.
"""

import subprocess
import sys

import smart_tagging


def test_the_package_is_actually_installed():
    """src-layout exists so that a broken install cannot hide behind the cwd.

    If the package were merely a directory on sys.path, importlib.metadata would
    find no distribution and the version would fall back to the sentinel.
    """
    assert smart_tagging.__version__ != "0.0.0+uninstalled", (
        "smart_tagging is importable but not installed — run: uv pip install -e ."
    )


def test_importing_the_package_does_not_pull_in_torch():
    """CI installs the package without the `local` extra, so the base import
    graph must stay torch-free.

    Run in a subprocess on purpose: by the time this test executes, the pytest
    session may already have imported torch for unrelated reasons, which would
    make an in-process check pass for the wrong reason.
    """
    probe = "import smart_tagging, sys; print('torch' in sys.modules)"
    result = subprocess.run(
        [sys.executable, "-c", probe],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "False", (
        "importing smart_tagging pulled in torch; move that import inside the "
        "function that needs it"
    )
