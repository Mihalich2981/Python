def cropped_tuple(tpl, var):
    line = [str(j_val) for j_val in tpl]
    string = ''.join(line)
    a = string.find(var)
    b = string.find(var, a + 1)
    if (a >= 0) and (b >= 0):
        new_tpl = tuple(line[a:b + 1])
    elif (a >= 0) and (b < 0):
        new_tpl = tuple(line[a:])
    else:
        new_tpl = ()
    return new_tpl


my_tpl = (2, 1, 3, 4, 5, 9, 7, 1, 6, 8, 0)
elem = input('\nВведите случайный элемент: ')
print(cropped_tuple(my_tpl, elem))

# зачет!
