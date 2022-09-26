num_shelves = int(input('\nКол-во палок: '))
num_throws = int(input('Кол-во бросков: '))
row_shelves = 'I' * num_shelves
for i_throw in range(1, num_throws + 1):
    print('Бросок', i_throw, '. Сбиты палки с номера', end=' ')
    from_num = int(input())
    by_num = int(input('по номер '))
    row_shelves = row_shelves[:from_num - 1] + '.' * (by_num - from_num + 1) + row_shelves[by_num:]
print('\nРезультат:', row_shelves)

# зачет!
