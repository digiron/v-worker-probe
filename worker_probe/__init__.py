"""Minimal synthetic package. A worker's synthetic task is to add a documented
function plus a passing test to this package and open a PR."""


def greet(name: str) -> str:
    """Return a greeting for ``name`` (the baseline function shipped with the repo)."""
    return f"hello, {name}"


def shout(name: str) -> str:
    """Return greet(name) upper-cased."""
    return greet(name).upper()


def farewell(name: str) -> str:
    """Return a farewell message for *name*.

    Parameters
    ----------
    name:
        The name of the person being bid farewell.  Leading/trailing
        whitespace is stripped before use.

    Returns
    -------
    str
        A farewell string of the form ``"goodbye, <name>"``.

    Raises
    ------
    TypeError
        If *name* is not a ``str``.
    ValueError
        If *name* is empty or whitespace-only after stripping.

    Examples
    --------
    >>> farewell("Alice")
    'goodbye, Alice'
    >>> farewell("  Bob  ")
    'goodbye, Bob'
    """
    if not isinstance(name, str):
        raise TypeError(f"name must be a str, got {type(name).__name__!r}")
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty or whitespace-only")
    return f"goodbye, {name}"
