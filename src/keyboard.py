from src.item import Item


class MixinLang:
    """Миксин-класс для изменения и хранения раскладки клавиатуры"""

    def __init__(self, language="EN"):
        """иницилизатор с языком по-умолчанию"""
        self.__language = language

    @property
    def language(self):
        """выводит раскладку клавиатуры"""
        return self.__language

    def change_lang(self):
        """метод для изменения раскладки клавиатуры"""
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):
    """класс для представления клавиатуры в магазине, дочерний класс Item """

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self, language)