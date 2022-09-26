def pr_key(lst):
    return lst[1][0] * 100000000 - lst[1][1]


records = int(input('\nСколько записей вносится в протокол? '))
print('Записи (результат и имя):')
protocol = {}
for time in range(records):
    result, name = input(f'{time + 1} запись: ').split()
    result = int(result)
    if name in protocol:
        if result > protocol[name][0]:
            protocol[name][0] = result
            protocol[name][1] = time
    else:
        protocol[name] = [result, time]
pr_lst = list(protocol.items())
pr_lst.sort(key=pr_key, reverse=True)
print('\nИтоги соревнований:')
for place in range(3):
    print(f'{place + 1} место. {pr_lst[place][0]} ({pr_lst[place][1][0]})')

# зачет!
