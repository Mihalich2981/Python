my_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'\nОригинальный список: {my_lst}')
# Вариант 1
lst_1 = [my_lst[i_key] for i_key in range(0, len(my_lst), 2)]
lst_2 = [my_lst[j_key] for j_key in range(1, len(my_lst), 2)]
new_lst_1 = [i_elem for i_elem in zip(lst_1, lst_2)]
print(f'Новый список: {new_lst_1}')
# Вариант 2
new_lst_2 = [(my_lst[i_key], my_lst[i_key + 1]) for i_key in range(0, len(my_lst), 2)]
print(f'Новый список: {new_lst_2}')

# зачет!
