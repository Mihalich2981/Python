def right_shift(simple_list):
    var_list = [simple_list[-1]]
    for i in range(len(simple_list) - 1):
        var_list.append(simple_list[i])
    return ''.join(var_list)


first_line = input('\nПервая строка: ')
second_line = input('Вторая строка: ')
if first_line == second_line:
    print('\nПервая строка равна второй строке')
else:
    for shift in range(1, len(first_line)):
        first_line = right_shift(list(first_line))
        if second_line == first_line:
            print('\nПервая строка получается из второй со сдвигом', shift)
            break
    else:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')

# зачет!
