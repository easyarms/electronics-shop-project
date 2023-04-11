"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

test_item = Item("Холодильник", 25000, 15)


def test_calculate_total_price():
    total_price = test_item.calculate_total_price()
    assert total_price == 375000


def test_apply_discount():
    Item.pay_rate = 0.15
    test_item.apply_discount()
    discount_price = test_item.price
    assert discount_price == 3750
