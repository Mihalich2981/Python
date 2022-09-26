def sort_list(nums_list):
    for mini in range(len(nums_list)):
        for var in range(mini, len(nums_list)):
            if nums_list[var] < nums_list[mini]:
                nums_list[var], nums_list[mini] = nums_list[mini], nums_list[var]


one_class = list(range(160, 177, 2))
two_class = list(range(162, 181, 3))
one_class.extend(two_class)
sort_list(one_class)
# Можно и одной встроенной командой, без функции: one_class.sort()
print('\nОтсортированный список:', one_class)

# зачет!
