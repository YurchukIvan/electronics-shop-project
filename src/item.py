import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join("src", "items.csv")  # путь к csv-файлу

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        with open(cls.CSV_PATH, encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for line in reader:
                item = cls(line['name'], float(line['price']), int(line['quantity']))

    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(string))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.quantity = quantity
        self.price = price
        self.__name = name
        self.all.append(self)

    def __repr__(self):
        """отображение информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """отображение информации об объекте класса для пользователей"""
        return f"{self.__name}"

    @property
    def name(self):
        """Возвращает имя"""
        return self.__name

    @name.setter
    def name(self, name):
        """Обрезает имя, если оно больше 10 символов"""
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate