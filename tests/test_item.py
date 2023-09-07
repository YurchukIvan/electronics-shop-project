import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def fix_item_class():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fix_phone_class():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(fix_item_class):
    """Общая стоимость товара = кол-во * на стоимость"""
    assert fix_item_class.calculate_total_price() == 200000


def test_apply_discount(fix_item_class):
    """При применении скидки цена товара становится меньше"""
    fix_item_class.pay_rate = 0.7
    fix_item_class.apply_discount()
    assert fix_item_class.price == 7000.0


def test_all(fix_item_class):
    """аргумент self.all добавляет экземпляры класса в список при инициализации"""
    assert type(fix_item_class.all) is list
    assert bool(fix_item_class.all) is True


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


def test_repr(fix_item_class):
    """тест repr"""
    assert repr(fix_item_class) == "Item('Смартфон', 10000, 20)"


def test_str(fix_item_class):
    """тест str"""
    assert str(fix_item_class) == 'Смартфон'


def test_add(fix_item_class, fix_phone_class):
    """тест сложения родственных классов"""
    assert fix_item_class + fix_phone_class == 25
    assert fix_phone_class + fix_phone_class == 10
    with pytest.raises(ValueError):
        assert fix_phone_class + 5 == 'Складывать можно только объекты Item и дочерние от них.'
        assert fix_item_class + 5 == 'Складывать можно только объекты Item и дочерние от них.'