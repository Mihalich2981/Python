print('\nВариант 1 (класс-итератор)')


class SquaresNumbers:
    def __init__(self, number: int) -> None:
        self.__number = number
        self.__counter = 0

    def __iter__(self) -> iter:
        self.__counter = 0
        return self

    def __next__(self) -> int:
        if self.__counter < self.__number:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration()


my_iter = SquaresNumbers(number=5)
for num in my_iter:
    print(num, end=' ')


print('\n\nВариант 2 (функция-генератор)')


def squares_numbers(number: int) -> int:
    for i_num in range(number):
        yield (i_num + 1) ** 2


nums = squares_numbers(number=10)
for i_val in nums:
    print(i_val, end=' ')


print('\n\nВариант 3 (генераторное выражение)')

squares_num = (num ** 2 for num in range(1, 15))
for j_num in squares_num:
    print(j_num, end=' ')
print()

# зачет!
