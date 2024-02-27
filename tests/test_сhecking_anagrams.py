"""
Задача: Проверка на анаграммы

Напишите функцию `are_anagrams(str1: str, str2: str) -> bool`,
которая принимает две строки и возвращает `True`,
если они являются анаграммами друг друга, и `False` в противном случае.
Анаграммы - это слова или фразы, образованные путем перестановки букв другого слова или
фразы, используя все исходные буквы ровно один раз.

Примеры:
are_anagrams("listen", "silent")  # Возвращает True
are_anagrams("hello", "world")    # Возвращает False
"""
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
