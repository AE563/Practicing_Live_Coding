import pytest
from src.сhecking_anagrams import are_anagrams


@pytest.mark.parametrize("str1, str2, expected", [
    ("listen", "silent", True),
    ("hello", "world", False),
    ("Abc", "BCa", True),
    ("Abc", "BCaD", False),
    ("Abc", "BC", False),
])
def test_are_anagrams(str1, str2, expected):
    assert are_anagrams(str1, str2) == expected, \
        f"Expected: {expected}, got: {are_anagrams(str1, str2)}"
