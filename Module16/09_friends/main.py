num_friends = int(input('\nКол-во друзей: '))
receipts = int(input('Долговых расписок: '))
friends_list = []

for _ in range(num_friends):
    friends_list.append(0)

for number in range(receipts):
    print('\n', number + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    summa = int(input('Сколько: '))
    friends_list[to_whom - 1] -= summa
    friends_list[from_whom - 1] += summa

print('\nБаланс друзей: ')
for index in range(len(friends_list)):
    print(index + 1, ':', friends_list[index])

# зачет!
