import pytest
from src.vowel_counter import count_vowels


@pytest.mark.parametrize('text, expected', [
    ("Hello", 2),
    ('AeIou', 5),
    ("Python is awesome", 6),
    ("Try to solve this task", 5),
    ("bcdfghjklmnpqrstvwxyz", 0)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected, \
        f"Expected {expected}, got {count_vowels(text)}"
