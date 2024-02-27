"""
Задача: Счетчик гласных
Напишите функцию count_vowels,
которая принимает строку и возвращает количество гласных букв (a, e, i, o, u) в строке.
Гласные буквы могут быть как в верхнем, так и в нижнем регистре.

Пример:
assert count_vowels("Hello") == 2
assert count_vowels("Python is awesome") == 6
assert count_vowels("Try to solve this task") == 5
"""
import pytest


def count_vowels(text: str) -> int:
    text = text.lower()
    count = 0
    for i in text:
        if i in '(aeiou)':
            count += 1
    return count


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
