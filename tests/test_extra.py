"""Comprehensive tests for farewell, whisper, repeat, reverse_greet, greet_all."""
import pytest

from worker_probe import farewell, greet_all, repeat, reverse_greet, whisper


# ---------------------------------------------------------------------------
# farewell
# ---------------------------------------------------------------------------

class TestFarewell:
    def test_basic(self):
        assert farewell("Alice") == "goodbye, Alice"

    def test_empty_name(self):
        assert farewell("") == "goodbye, "

    def test_single_char(self):
        assert farewell("Z") == "goodbye, Z"

    def test_whitespace_name(self):
        assert farewell("  ") == "goodbye,   "

    def test_numeric_string(self):
        assert farewell("123") == "goodbye, 123"

    def test_unicode_name(self):
        assert farewell("Ångström") == "goodbye, Ångström"


# ---------------------------------------------------------------------------
# whisper
# ---------------------------------------------------------------------------

class TestWhisper:
    def test_basic(self):
        assert whisper("Bob") == "hello, bob"

    def test_already_lower(self):
        assert whisper("bob") == "hello, bob"

    def test_all_upper(self):
        assert whisper("BOB") == "hello, bob"

    def test_mixed_case(self):
        assert whisper("bOb") == "hello, bob"

    def test_empty_name(self):
        assert whisper("") == "hello, "

    def test_single_char(self):
        assert whisper("A") == "hello, a"

    def test_unicode(self):
        # lower-case of already-lower unicode stays lower
        assert whisper("léa") == "hello, léa"


# ---------------------------------------------------------------------------
# repeat
# ---------------------------------------------------------------------------

class TestRepeat:
    def test_basic(self):
        assert repeat("Carol", 3) == ["hello, Carol"] * 3

    def test_once(self):
        assert repeat("Carol", 1) == ["hello, Carol"]

    def test_zero(self):
        assert repeat("Carol", 0) == []

    def test_negative(self):
        assert repeat("Carol", -5) == []

    def test_empty_name(self):
        assert repeat("", 2) == ["hello, ", "hello, "]

    def test_empty_name_zero(self):
        assert repeat("", 0) == []

    def test_large_n(self):
        result = repeat("X", 100)
        assert len(result) == 100
        assert all(r == "hello, X" for r in result)


# ---------------------------------------------------------------------------
# reverse_greet
# ---------------------------------------------------------------------------

class TestReverseGreet:
    def test_basic(self):
        assert reverse_greet("Dave") == "hello, evaD"

    def test_single_char(self):
        assert reverse_greet("A") == "hello, A"

    def test_empty_name(self):
        assert reverse_greet("") == "hello, "

    def test_palindrome(self):
        assert reverse_greet("Ana") == "hello, anA"

    def test_spaces(self):
        assert reverse_greet("ab cd") == "hello, dc ba"

    def test_numbers(self):
        assert reverse_greet("123") == "hello, 321"


# ---------------------------------------------------------------------------
# greet_all
# ---------------------------------------------------------------------------

class TestGreetAll:
    def test_basic(self):
        assert greet_all(["Eve", "Frank"]) == ["hello, Eve", "hello, Frank"]

    def test_empty_list(self):
        assert greet_all([]) == []

    def test_single_item(self):
        assert greet_all(["Grace"]) == ["hello, Grace"]

    def test_empty_string_in_list(self):
        assert greet_all([""]) == ["hello, "]

    def test_mixed_with_empty(self):
        assert greet_all(["Eve", "", "Frank"]) == [
            "hello, Eve",
            "hello, ",
            "hello, Frank",
        ]

    def test_preserves_order(self):
        names = ["c", "b", "a"]
        result = greet_all(names)
        assert result == ["hello, c", "hello, b", "hello, a"]

    def test_all_empty_strings(self):
        assert greet_all(["", ""]) == ["hello, ", "hello, "]

    def test_large_list(self):
        names = [str(i) for i in range(50)]
        result = greet_all(names)
        assert len(result) == 50
        assert result[0] == "hello, 0"
        assert result[49] == "hello, 49"
