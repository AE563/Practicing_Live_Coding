import pytest
from src.spreading_words import spreading_words


@pytest.mark.parametrize("text, exception", [
    ("Hello", "olleH"),
    ("Python is awesome", "nohtyP si emosewa"),
    ("Try to solve this task", "yrT ot evlos siht ksat")
])
def test_spreading_words(text, exception):
    assert spreading_words(text) == exception
