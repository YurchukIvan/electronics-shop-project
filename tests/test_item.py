"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def fix_item_class():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(fix_item_class):
    """Общая стоимость товара = кол-во * на стоимость"""
    assert fix_item_class.calculate_total_price() == 200000

def test_apply_discount(fix_item_class):
    """При применении скидки цена товара становится меньше"""
    fix_item_class.pay_rate = 0.7
    fix_item_class.apply_discount()
    assert fix_item_class.price == 7000.0

def test_instantiate_from_csv():
    """класс-метод инициализирует экземпляры из файла csv"""
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_string_to_number():
    """возвращает число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_name(fix_item_class):
    """перезаписывает приватный атрибут name, сокращает строку до 10 символов"""
    item = fix_item_class
    item.name = 'Телефон'
    assert item.name == 'Телефон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'