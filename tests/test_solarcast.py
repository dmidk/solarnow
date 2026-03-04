"""Basic tests for the solarcast package."""

import solarcast


def test_version():
    """Ensure the package exposes a version string."""
    assert isinstance(solarcast.__version__, str)
    assert len(solarcast.__version__) > 0
