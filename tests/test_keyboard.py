import pytest
from src.keyboard import Keyboard


@pytest.fixture
def fix_keyboard_class():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(fix_keyboard_class):
    """тест инициализации"""
    assert str(fix_keyboard_class) == "Dark Project KD87A"
    # тест языка по-умолчанию
    assert str(fix_keyboard_class.language) == "EN"


def test_change_lang(fix_keyboard_class):
    """тест смены языка"""
    fix_keyboard_class.change_lang()
    assert str(fix_keyboard_class.language) == "RU"
    # Сделали RU -> EN -> RU
    fix_keyboard_class.change_lang().change_lang()
    assert str(fix_keyboard_class.language) == "RU"
    with pytest.raises(AttributeError):
        fix_keyboard_class.language = 'CH'