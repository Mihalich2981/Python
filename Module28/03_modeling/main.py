from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """
    Абстрактный базовый класс Figure
    """

    @abstractmethod
    def perimeter(self) -> None:
        pass

    @abstractmethod
    def area(self) -> None:
        pass


class Triangle(Figure):
    """
    Класс Triangle (треугольник) родительский класс Figure
    Args:
        height (int): высота треугольника
        width (int): основание (сторона) треугольника
    """

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    @property
    def height(self):
        """Геттер возвращающий высоту треугольника"""
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        """Сеттер устанавливающий положительную высоту треугольника,
        иначе выдает исключение"""
        if height > 0:
            self._height = height
        else:
            raise Exception('Недопустимая величина')

    @property
    def width(self):
        """Геттер возвращающий основание (сторону) треугольника"""
        return self._width

    @width.setter
    def width(self, width: int):
        """Сеттер устанавливающий положительное основание (сторону) треугольника,
        иначе выдает исключение"""
        if width > 0:
            self._width = width
        else:
            raise Exception('Недопустимая величина')

    def perimeter(self) -> float:
        """
        Метод вычисления периметра треугольника по высоте и основанию
        Returns:
            периметр треугольника
        """
        return self._width + 2 * math.sqrt((self._width / 2) ** 2 + self._height ** 2)

    def area(self) -> float:
        """
        Метод вычисления площади треугольника по высоте и основанию
        Returns:
            площадь треугольника
        """
        return self._width * self._height / 2


class Square(Figure):
    """
    Класс Square (квадрат) родительский класс Figure
    Args:
        size (int): сторона квадрата
    """

    def __init__(self, size: int) -> None:
        self.size = size

    @property
    def size(self):
        """Геттер возвращающий основание (сторону) квадрата"""
        return self._size

    @size.setter
    def size(self, size: int):
        """Сеттер устанавливающий положительное основание (сторону) квадрата,
        иначе выдает исключение"""
        if size > 0:
            self._size = size
        else:
            raise Exception('Недопустимая величина')

    def perimeter(self) -> float:
        """
        Метод вычисления периметра квадрата по его стороне
        Returns:
            периметр квадрата
        """
        return 4 * self._size

    def area(self) -> float:
        """
        Метод вычисления площади квадрата по его стороне
        Returns:
            площадь квадрата
        """
        return self._size ** 2


class Pyramid(Triangle, Square):
    """Класс Pyramid (пирамида) родительский класс Triangle"""

    def __init__(self, height: int, width: int) -> None:
        super().__init__(height, width)
        self.size = width

    def area(self) -> float:
        """
        Метод вычисления площади пирамиды по высоте и основанию
        Returns:
            площадь пирамиды
        """
        return Triangle.area(self) * 4 + Square.area(self)


class Cube(Square):
    """Класс Cube (куб) родительский класс Square"""
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def area(self) -> float:
        """
        Метод вычисления площади куба по стороне
        Returns:
            площадь куба
        """
        return super().area() * 6


t = Triangle(height=5, width=7)
print('Площадь треугольника', t.area())
print('Периметр треугольника', t.perimeter())
k = Square(size=8)
print('Площадь квадрата', k.area())
print('Периметр квадрата', k.perimeter())
c = Cube(size=10)
print('Площадь куба', c.area())
p = Pyramid(height=4, width=8)
print('Площадь пирамиды', p.area())

# зачет!
