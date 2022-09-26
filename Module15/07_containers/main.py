quantity = int(input('\nКол-во контейнеров: '))
control_weight = 199
weights_list = []

for _ in range(quantity):
    while True:
        weight = int(input('Введите вес контейнера: '))
        if weight <= control_weight:
            control_weight = weight
            break
        print('Неверно ввели вес контейнера!')
    weights_list.append(weight)

new_weight = int(input('\nВведите вес нового контейнера: '))

for i in range(quantity):
    if weights_list[i] < new_weight:
        break
print('\nНомер, куда встанет новый контейнер:', i + 1)

# зачет!
