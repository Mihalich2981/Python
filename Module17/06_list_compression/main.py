import random


def zero_end(nums_list):
    count = 0
    for i in range(len(nums_list)):
        if nums_list[i] == 0:
            count += 1
            for var in range(i + 1, len(nums_list)):
                nums_list[var - 1], nums_list[var] = nums_list[var], nums_list[var - 1]
    count //= 2
    return nums_list[:-count]


num = int(input('\nВведите длину списка: '))
lst_nums = [random.randint(-5, 5) for _ in range(num)]
print('Список:', lst_nums)
lst_nums = zero_end(lst_nums)

# Вариант 1: lst_nums = [i for i in lst_nums if i]

print('Сжатый список:', lst_nums)

# зачет!
