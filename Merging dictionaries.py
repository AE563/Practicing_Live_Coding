"""
Задача: Слияние словарей
Напишите функцию `merge_dicts`, которая объединяет два словаря в один.
Если ключи повторяются, то значения из второго словаря перезаписывают значения первого.

Пример использования:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Ожидаемый результат: {'a': 1, 'b': 3, 'c': 4}

Примечание:
- Исходные словари `dict1` и `dict2` должны оставаться неизменными.
- Результат должен быть новым словарем, содержащим объединение исходных словарей.
"""
import pytest


# Функция объединения словарей
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


# Параметризованные тесты для проверки объединения словарей
@pytest.mark.parametrize("dict1, dict2, expected", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 1, 'b': 3, 'c': 4}),
    ({'x': 10, 'y': 20}, {'z': 30, 'y': 40}, {'x': 10, 'y': 40, 'z': 30}),
    ({}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2}, {}, {'a': 1, 'b': 2}),
    ({}, {}, {})
])
def test_merge_dicts(dict1, dict2, expected):
    assert merge_dicts(dict1, dict2) == expected, \
        f'Ожидаемый ответ {expected}, а получили {merge_dicts(dict1, dict2)}'


# Тест результат должен быть новым словарем
@pytest.mark.parametrize("dict1, dict2", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}),
    ({'x': 10, 'y': 20}, {'z': 30, 'y': 40}),
])
def test_merge_dicts_new_dict(dict1, dict2):
    result = merge_dicts(dict1, dict2)
    assert result != dict1, 'Результат не должен быть исходным словарем dict1'
    assert result != dict2, 'Результат не должен быть исходным словарем dict2'
