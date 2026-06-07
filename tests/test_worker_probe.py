from worker_probe import greet, shout, farewell


def test_greet():
    assert greet("v") == "hello, v"


def test_shout():
    assert shout("v") == "HELLO, V"


def test_farewell():
    assert farewell("v") == "goodbye, v"
