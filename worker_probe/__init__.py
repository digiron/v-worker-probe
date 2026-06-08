"""Minimal synthetic package. A worker's synthetic task is to add a documented
function plus a passing test to this package and open a PR."""


def greet(name: str) -> str:
    """Return a greeting for ``name`` (the baseline function shipped with the repo)."""
    return f"hello, {name}"


def shout(name: str) -> str:
    """Return greet(name) upper-cased."""
    return greet(name).upper()


def whisper(name: str) -> str:
    """Return a quiet greeting for ``name``.

    Produces the same text as :func:`greet` but in lower-case, suitable for
    contexts where a subdued response is preferred.

    Args:
        name: The recipient's name.

    Returns:
        A lower-cased greeting string, e.g. ``"hello, alice"``.
    """
    return greet(name).lower()
