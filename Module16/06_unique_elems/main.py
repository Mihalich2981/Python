first_list = [1, 2, 3]
second_list = [2, 4, 6, 3, 3, 2, 1]
new_first_list = []
first_list.extend(second_list)
# Можно так: new_first_list = list(set(first_list))
# или так: while же - не является условным оператором!
while first_list:
    num = first_list[0]
    k = first_list.count(num)
    new_first_list.append(num)
    for _ in range(k):
        first_list.remove(num)
print('\nНовый первый список с уникальными элементами:', new_first_list)

# зачет!
