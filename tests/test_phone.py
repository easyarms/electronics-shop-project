import pytest

from src.phone import Phone

test_phone = Phone("Samsung S24 Ultra", 150_000, 10, 5)


def test__repr__():
    assert repr(test_phone) == "Phone('Samsung S24 Ultra', 150000, 10, 5)"


def number_of_sim():
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1
    with pytest.raises(Exception):
        test_phone.number_of_sim = 0 or -1
