import random


def f(x: int, y: int) -> float:
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x: int, y: int) -> float:
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as file_2:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            my_list = [str(i) for i in my_list]
            file_2.write(f"{', '.join(my_list)}\n")
# TODO я вроде писал, что можно ловить текст ошибки так except FileNotFoundError as e:
except FileNotFoundError:
    print("Файл не найден.")
except ValueError:
    print("Неверно заданы числа.")
except TypeError:
    print("В файле с расширением 'txt', записываются только строчные элементы.")
except ZeroDivisionError:
    print("Нельзя делить на ноль.")

# зачет!
