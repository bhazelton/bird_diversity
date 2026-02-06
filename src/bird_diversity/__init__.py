import contextlib
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from setuptools_scm import get_version

try:
    # get accurate version for developer installs
    # must point to folder that contains the .git file!
    version_str = get_version(Path(__file__).parent.parent.parent)

    __version__ = version_str

except (LookupError, ImportError):  # pragma: no cover
    # Set the version automatically from the package details.
    # don't set anything if the package is not installed
    with contextlib.suppress(PackageNotFoundError):
        __version__ = version("bird_diversity")
