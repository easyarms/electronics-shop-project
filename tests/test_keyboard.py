import pytest

from src.keyboard import Keyboard

test_keyboard = Keyboard('Apple Magic Keyboard', 17_000, 12)


def test__str__():
    assert str(test_keyboard) == 'Apple Magic Keyboard'


def test_change_lang():
    assert str(test_keyboard.language) == 'EN'
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == 'RU'
    test_keyboard.change_lang().change_lang().change_lang()
    assert str(test_keyboard.language) == 'EN'
