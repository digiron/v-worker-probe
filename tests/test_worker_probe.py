from worker_probe import greet


def test_greet():
    assert greet("v") == "hello, v"
