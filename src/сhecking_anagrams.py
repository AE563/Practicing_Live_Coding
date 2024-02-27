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


def are_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    for i in str1:
        if i not in str2:
            return False
    return True
