"""
Разворот слов в строке

Задача: Разворот слов в строке
Напишите функцию spreading_words,
которая принимает строку и возвращает строку слова в которой перевернуты.


Пример:
assert spreading_words("Hello") == "olleH"
assert spreading_words("Python is awesome") == "nohtyP si emosewa"
assert spreading_words("Try to solve this task") == "yrT ot evlos siht ksat"
"""


def spreading_words(text: str) -> str:
    result = ''
    count_words = 0
    text_split = text.split()
    len_text_split = len(text_split)
    for i in text_split:
        count_words += 1
        if count_words == len_text_split:
            result += i[::-1]
            return result
        result += i[::-1] + " "
