number_skates = int(input('\nКол-во коньков: '))
pair_list = []
coincidence = 0

for i_elem in range(number_skates):
    print('Размер', i_elem + 1, 'пары:', end=' ')
    size_pair = int(input())
    pair_list.append(size_pair)

number_people = int(input('\nКол-во людей: '))
foot_list = []

for i_elem in range(number_people):
    print('Размер ноги', i_elem + 1, 'человека:', end=' ')
    size_foot = int(input())
    foot_list.append(size_foot)

# Вариант 1

for i_elem in pair_list:
    for i_num in foot_list:
        if i_elem == i_num:
            coincidence += 1
            foot_list.remove(i_num)
            break
    if not foot_list:
        break

# Вариант 2

# coincidence = len(list(set(pair_list) & set(foot_list)))

print('\nНаибольшее кол-во людей, которые могут взять ролики:', coincidence)

# зачет!
