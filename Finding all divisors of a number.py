"""
Задача: Поиск всех делителей числа

Напиши функцию, которая принимает на вход целое число
и возвращает список всех его делителей (включая 1 и само число).
Если число является простым, возвращаем список из двух элементов: 1 и само число.

Примеры:

divisors(12) должно вернуть [1, 2, 3, 4, 6, 12]
divisors(7) должно вернуть [1, 7]
divisors(31) должно вернуть [1, 31]
"""
import pytest


def divisors(num: int) -> list:
    result_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            result_list.append(i)
    return result_list


@pytest.mark.parametrize("num, expected_result", [
    (12, [1, 2, 3, 4, 6, 12]),
    (7, [1, 7]),
    (31, [1, 31])
])
def test_divisors(num, expected_result):
    assert divisors(num) == expected_result, \
        f'Ожидаемый результат {expected_result}, получили {divisors(num)}'
