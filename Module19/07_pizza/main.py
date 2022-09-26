nums = int(input('\nВведите кол-во заказов: '))
orders = dict()
for i_num in range(nums):
    fio, pizza, pieces = input(f'{i_num + 1} заказ: ').title().split()
    pieces = int(pieces)
    if fio not in orders:
        orders[fio] = {pizza: pieces}
    else:
        if pizza not in orders[fio]:
            orders[fio].update({pizza: pieces})
        else:
            orders[fio][pizza] += pieces
print()
for i_num in sorted(orders.keys()):
    print(f'{i_num}:')
    for j_num in sorted(orders[i_num].keys()):
        print('    ', j_num, orders[i_num][j_num])

# зачет!

