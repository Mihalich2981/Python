people = int(input('\nКол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек\n')
people_list = list(range(1, people + 1))
out = 0
for _ in range(people - 1):
    print('Текущий круг людей', people_list)
    start = out % len(people_list)
    out = (start + number - 1) % len(people_list)
    print('Начало счёта с номера', people_list[start])
    print('Выбывает человек под номером', people_list[out], '\n')
    people_list.remove(people_list[out])
print('Остался человек под номером', people_list[0])

# зачет!
