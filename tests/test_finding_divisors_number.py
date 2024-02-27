import pytest
from src.finding_divisors_number import divisors


@pytest.mark.parametrize("num, expected_result", [
    (12, [1, 2, 3, 4, 6, 12]),
    (7, [1, 7]),
    (31, [1, 31])
])
def test_divisors(num, expected_result):
    assert divisors(num) == expected_result, \
        f'Ожидаемый результат {expected_result}, получили {divisors(num)}'
