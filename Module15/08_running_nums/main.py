def right_shift(num, simple_list):
    length = len(simple_list)
    var_list = []
    for _ in range(num):
        var_list.append(simple_list[-1])
        for i in range(length - 1):
            var_list.append(simple_list[i])
        simple_list = var_list
        var_list = []
    return simple_list


initial_list = [1, 4, -3, 0, 10]
shift = int(input('Сдвиг: '))
print('Изначальный список:', initial_list)

initial_list = right_shift(shift, initial_list)

print('Сдвинутый список:', initial_list)

# зачет!
