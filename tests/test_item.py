"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_item = Item("Холодильник", 25000, 15)
over_ten_simbols = 'long_name_of_item'


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

# def test_name_length():
#     Item.name_length(over_ten_simbols)
#     assert 'Длина наименования товара не может быть более 10-ти символов'
