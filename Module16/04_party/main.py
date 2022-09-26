guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    go = input('Гость пришёл или ушёл? ').lower()
    if go == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print('Привет,', name, '!')
        else:
            print('Прости,', name, ', но мест нет.')
    elif go == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока,', name, '!')
    elif go == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('Что-то пошло не так! Попробуте, ещё раз.')

# зачет!
