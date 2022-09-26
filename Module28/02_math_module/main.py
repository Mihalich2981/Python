import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Метод, нахождение длины окружности
        Args:
            radius: float - радиус

        Returns: float - длина окружности
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
         Метод, нахождение площади окружности
        Args:
            radius: float - радиус

        Returns: float - площадь окружности
        """
        return math.pi * radius ** 2

    @classmethod
    def cube_vlm(cls, side: float) -> float:
        """
        Метод, нахождение объема куба
        Args:
            side: float - длина стороны куба

        Returns: float - объем куба
        """
        return side ** 3

    @classmethod
    def sphere_sq_area(cls, radius: float) -> float:
        """
        Метод, нахождение площади поверхности сферы
        Args:
            radius: float - радиус

        Returns: float - площадь поверхности сферы
        """
        return 8 * math.pi * radius


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

# зачет!
