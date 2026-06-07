"""Minimal synthetic package. A worker's synthetic task is to add a documented
function plus a passing test to this package and open a PR."""


def greet(name: str) -> str:
    """Return a greeting for ``name`` (the baseline function shipped with the repo)."""
    return f"hello, {name}"


def shout(name: str) -> str:
    """Return greet(name) upper-cased."""
    return greet(name).upper()


def farewell(name: str) -> str:
    """Return a farewell message for ``name``.

    Parameters
    ----------
    name:
        The name to address.  An empty string is accepted and yields a
        generic farewell.

    Returns
    -------
    str
        A farewell string of the form ``"goodbye, <name>"`` or
        ``"goodbye, "`` when *name* is empty.

    Examples
    --------
    >>> farewell("Alice")
    'goodbye, Alice'
    >>> farewell("")
    'goodbye, '
    """
    return f"goodbye, {name}"


def whisper(name: str) -> str:
    """Return a quietly-spoken greeting for ``name``.

    The greeting is the same as :func:`greet` but converted to lower-case,
    ensuring a soft, whispered tone regardless of the capitalisation of
    *name*.

    Parameters
    ----------
    name:
        The name to address.  An empty string is accepted.

    Returns
    -------
    str
        Lower-case greeting of the form ``"hello, <name>"``.

    Examples
    --------
    >>> whisper("Bob")
    'hello, bob'
    >>> whisper("BOB")
    'hello, bob'
    >>> whisper("")
    'hello, '
    """
    return greet(name).lower()


def repeat(name: str, n: int) -> list[str]:
    """Return a list containing *n* copies of ``greet(name)``.

    Parameters
    ----------
    name:
        The name to greet.  An empty string is accepted.
    n:
        How many times to repeat the greeting.  Values of zero or below
        yield an empty list rather than raising an error.

    Returns
    -------
    list[str]
        A list of *n* identical greeting strings, or ``[]`` when *n* <= 0.

    Examples
    --------
    >>> repeat("Carol", 3)
    ['hello, Carol', 'hello, Carol', 'hello, Carol']
    >>> repeat("Carol", 0)
    []
    >>> repeat("Carol", -1)
    []
    >>> repeat("", 2)
    ['hello, ', 'hello, ']
    """
    if n <= 0:
        return []
    return [greet(name)] * n


def reverse_greet(name: str) -> str:
    """Return a greeting where *name* is spelled backwards.

    Parameters
    ----------
    name:
        The name to reverse and then address.  An empty string is accepted
        and yields a greeting with an empty reversed name (i.e. the same as
        ``greet("")``).

    Returns
    -------
    str
        A greeting of the form ``"hello, <reversed name>"``.

    Examples
    --------
    >>> reverse_greet("Dave")
    'hello, evaD'
    >>> reverse_greet("A")
    'hello, A'
    >>> reverse_greet("")
    'hello, '
    """
    return greet(name[::-1])


def greet_all(names: list[str]) -> list[str]:
    """Return a list of greetings for every name in *names*.

    Parameters
    ----------
    names:
        A list of name strings.  An empty list returns an empty list.
        Individual names that are empty strings are accepted and produce
        ``"hello, "`` entries in the result.

    Returns
    -------
    list[str]
        A list of greeting strings, one per entry in *names*, in the same
        order.

    Examples
    --------
    >>> greet_all(["Eve", "Frank"])
    ['hello, Eve', 'hello, Frank']
    >>> greet_all([])
    []
    >>> greet_all([""])
    ['hello, ']
    >>> greet_all(["Eve", "", "Frank"])
    ['hello, Eve', 'hello, ', 'hello, Frank']
    """
    return [greet(name) for name in names]
