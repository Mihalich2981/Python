name = input('\nВведите Ваше имя: ')
while True:
    print('\nВыберете одно из действий:\n'
          '     1. Посмотреть текущий текст чата.\n'
          '     2. Написать сообщение.')
    action = input('Введите 1 или 2: ')
    print()
    if action == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Увы! Пока ничего нет...')
    elif action == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name}: {new_message}\n')
    else:
        print('Ошибка! Нет такого в действия!')

# зачет!
