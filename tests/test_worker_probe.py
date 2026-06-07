from worker_probe import greet, shout


def test_greet():
    assert greet("v") == "hello, v"


def test_shout():
    assert shout("v") == "HELLO, V"
