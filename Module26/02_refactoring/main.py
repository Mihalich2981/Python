list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def multiplication(find: int, lst_1: list, lst_2: list) -> tuple:
    for x in lst_1:
        for y in lst_2:
            result = x * y
            yield x, y, result
            if result == find:
                print('Found!!!')
                return


for num in multiplication(to_find, list_1, list_2):
    print(str(num)[1:-1])

# зачет!
