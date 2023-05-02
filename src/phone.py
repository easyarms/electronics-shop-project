from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество SIM-карт в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Getter для param: number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim > 0:
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"
