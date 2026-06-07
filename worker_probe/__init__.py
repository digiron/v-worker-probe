"""Minimal synthetic package. A worker's synthetic task is to add a documented
function plus a passing test to this package and open a PR."""


def greet(name: str) -> str:
    """Return a greeting for ``name`` (the baseline function shipped with the repo)."""
    return f"hello, {name}"


def shout(name: str) -> str:
    """Return greet(name) upper-cased."""
    return greet(name).upper()
