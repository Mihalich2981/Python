class Property:
    """
    Базовый класс имеет атрибут worth (стоимость), который передаётся в конструктор
    Args: worth (int): стоимость имущества
    """
    def __init__(self, worth):
        self.worth = worth


class Apartment(Property):
    """
    Класс Квартира, Родитель: Property
    Args: worth (int): стоимость квартиры
    """
    def tax(self):
        """
        Метод для вывода налога за квартиру
        :return: возвращает налог на квартиру в зависимости от её стоимости (float)
        """
        print(f'Налог на квартиру равен: {round(self.worth / 1000, 2)}')
        return round(self.worth / 1000, 2)


class Car(Property):
    """
    Класс Машина, Родитель: Property
    Args: worth (int): стоимость машины
    """
    def tax(self):
        """
        Метод для вывода налога за машину
        :return: возвращает налог на машину в зависимости от её стоимости (float)
        """
        print(f'Налог на машину равен: {round(self.worth / 200, 2)}')
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    """
    Класс Дача, Родитель: Property
    Args: worth (int): стоимость дачи
    """
    def tax(self):
        """
        Метод для вывода налога за дачу
        :return: возвращает налог на дачу в зависимости от её стоимости (float)
        """
        print(f'Налог на дачу равен: {round(self.worth / 500, 2)}')
        return round(self.worth / 500, 2)


money = int(input('Введите количество денег: '))
apartment_price = Apartment(worth=int(input('Какова стоимость квартиры: ')))
car_price = Car(worth=int(input('Какова стоимость машины: ')))
cottage_price = CountryHouse(worth=int(input('Какова стоимость дачи: ')))
summa_tax = apartment_price.tax() + car_price.tax() + cottage_price.tax()
if money >= summa_tax:
    print('\nВам хватает денег для уплаты всех налогов, остаток составляет:', money - summa_tax)
else:
    print(f'\nВам не хватает {summa_tax - money} для уплаты всех налогов.')

# зачет!
