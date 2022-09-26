import math


class Auto:
    """
    Базовый класс Auto, описывающий направление движения автомобиля
    Args:
        x (float) - передаётся координата Х
        y (float) - передаётся координата У
        fi (float) - угол направление движения
    """
    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist):
        """
        Метод расчета новых координат Х и У (новая точка)
        Attributes:
            dist (float) - расстояние в выбранном направлении
        """
        self.x = self.x + dist * math.sin(self.fi)
        self.y = self.y + dist * math.cos(self.fi)


class Bus(Auto):
    """
   Класс Bus , Родитель: Auto
    Args:
        x (float) - передаётся координата Х
        y (float) - передаётся координата У
        fi (float) - угол направление движения
        people (int) - счетчик людей в автобусе
        money (float) - сумма(количество) денег
    """
    def __init__(self, x, y, fi, people=0, money=0):
        super().__init__(x, y, fi)
        self.people = people
        self.money = money

    def enter(self, nums):
        """
        Метод увелечения людей в автобусе
        Attributes:
            nums (int) - количество вошедших людей
        """
        self.people += nums

    def exit(self, nums):
        """
        Метод уменьшения людей в автобусе
        Attributes:
            nums (int) - количество вышедших людей
        """
        if (self.people > 0) and (self.people >= nums):
            self.people -= nums
        else:
            self.people = 0

    def move(self, dist):
        """
        Метод расчета оплаты за проезд
        Attributes:
            dist (float) - расстояние, которое проехали пассажиры
        """
        self.money += self.people * dist

# зачет!
