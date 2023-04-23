import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.quantity * self.price
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Getter для param name
        """

        return self.__name

    @name.setter
    def name_length(self, new_name: str):
        """
        Проверяет длину наименования товара через param name.
        Длина должна быть не более 10 символов.
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара не может быть более 10-ти символов')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """

        cls.all = []
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                print(row)
                cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(value: str):
        if '.' in value:
            return int(float(value))
        return float(value)
