def sort(nums_list):
    for mini in range(len(nums_list)):
        for var in range(mini, len(nums_list)):
            if nums_list[var] < nums_list[mini]:
                nums_list[var], nums_list[mini] = nums_list[mini], nums_list[var]
    return nums_list


initial_list = [1, 4, -3, 0, 10]
print('\nИзначальный список:', initial_list)

initial_list = sort(initial_list)
print('\nОтсортированный список:', initial_list)

# С начало так сделал, не посмотрел внимательно на условие
# def min_num(num, nums_list):
#    mini = num
#    for var in nums_list:
#        if mini >= var:
#            mini = var
#    return mini
# def exception(num, nums_list):
#    new_nums_list = []
#    for i in nums_list:
#        if i != num:
#           new_nums_list.append(i)
#    return new_nums_list
# initial_list = [1, 4, -3, 0, 10]
# print('\nИзначальный список:', initial_list)
# sorted_list = []
# while initial_list:
#    minimum = min_num(initial_list[0], initial_list)
#    sorted_list.append(minimum)
#    initial_list = exception(minimum, initial_list)
#
# print('\nОтсортированный список:', sorted_list)

# зачет!
