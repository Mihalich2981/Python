nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [elem for group in nice_list for subgroup in group for elem in subgroup]
print('\n', nice_list)

# зачет!
