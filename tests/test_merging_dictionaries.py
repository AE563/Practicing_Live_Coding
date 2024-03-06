import pytest
from src.merging_dictionaries import merge_dicts


# Параметризованные тесты для проверки объединения словарей
@pytest.mark.parametrize("dict1, dict2, expected", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 1, 'b': 3, 'c': 4}),
    ({'x': 10, 'y': 20}, {'z': 30, 'y': 40}, {'x': 10, 'y': 40, 'z': 30}),
    ({}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2}, {}, {'a': 1, 'b': 2}),
    ({}, {}, {})
])
def test_merge_dicts(dict1, dict2, expected):
    assert merge_dicts(dict1, dict2) == expected


# Тест результат должен быть новым словарем
@pytest.mark.parametrize("dict1, dict2", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}),
    ({'x': 10, 'y': 20}, {'z': 30, 'y': 40}),
])
def test_merge_dicts_new_dict(dict1, dict2):
    result = merge_dicts(dict1, dict2)
    assert result != dict1, 'Результат не должен быть исходным словарем dict1'
    assert result != dict2, 'Результат не должен быть исходным словарем dict2'
