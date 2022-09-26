user = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def numbers_index(var):
    return [i_num for i_num, j_val in enumerate(var)]


def is_prime(num):
    lst = []
    for number in range(2, num):
        for prime in lst:
            if number % prime == 0:
                break
        else:
            lst.append(number)
    return lst


index = len(numbers_index(user))

if index < 3:
    print('Нет элементов, индекс которых - это простое число')
else:
    index_lst = is_prime(index)
    print(f'Список простых индексов: {index_lst}')

# зачет!
