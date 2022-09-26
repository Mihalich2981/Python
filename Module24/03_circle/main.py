import math


class Circle:
    pi = round(math.pi, 2)

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self) -> float:
        return self.pi * self.r ** 2

    def perimeter(self) -> float:
        return 2 * self.pi * self.r

    def scale(self, k) -> float:
        return self.r * k

    def intersection(self, other) -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


circle_1 = Circle(3, 3, 3)
circle_2 = Circle(0, 0, 1)
print('\nПлощадь равна:', circle_1.area())
print('Периметр равен:', circle_1.perimeter())
print(f'Увеличиваться в {circle_1.scale(5)} раз')
if circle_1.intersection(circle_2):
    print('Пересекается с другой окружностью')
else:
    print('С другой окружностью - не пересекается')

# зачет!
