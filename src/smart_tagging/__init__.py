"""AI smart tagging for fashion e-commerce catalogs.

Nothing heavy is imported here on purpose. Importing this package must not pull
in torch: CI installs no torch, and a module-level import would break it. The
modules that need it import it inside the functions that use it.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("smart-tagging")
except PackageNotFoundError:
    # Reached only when the package was never installed — e.g. someone put the
    # source tree on sys.path directly. Caught narrowly: a broader except would
    # hide a genuinely broken installation behind a plausible-looking version.
    __version__ = "0.0.0+uninstalled"

__all__ = ["__version__"]
