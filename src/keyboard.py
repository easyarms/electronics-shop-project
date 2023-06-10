from src.item import Item


class MixinChangeLang:

    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        """Getter для param: language"""

        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self


class Keyboard(Item, MixinChangeLang):
    """Класс для представления клавиатуры"""
    pass
