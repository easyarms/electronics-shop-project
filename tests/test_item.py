"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

test_item = Item("Холодильник", 25000, 15)
new_name = 'new_name'


def test_calculate_total_price():
    total_price = test_item.calculate_total_price()
    assert total_price == 375000


def test_apply_discount():
    Item.pay_rate = 0.15
    test_item.apply_discount()
    discount_price = int(test_item.price)
    assert discount_price == 3750


def test_string_to_number():
    str_value = '10.1'
    new_value = Item.string_to_number(str_value)
    assert new_value == 10


def test_name():
    test_item.name = 'new_name'
    assert test_item.name == 'new_name'
    with pytest.raises(Exception):
        test_item.name = 'super_new_name'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
