phonebook_dict = {
    ('Петров', 'Миша'): 88005556565,
    ('Петров', 'Денис'): 88003333333,
    ('Сидорова', 'Алёна'): 88005556565,
    ('Сидоров', 'Павел'): 88004445444,
    ('Иванов', 'Денис'): 88003338888,
    ('Егорова', 'Таня'): 88007778888,
    ('Ульянова', 'Алёна'): 88007777755
}

while True:
    action = input('\nВведите действие:\n"добавить" - добавить контакт\n"поиск" - поиск человека по фамилии:\n'
                   '').lower()
    if action == 'добавить':
        name = input('\nВведите имя: ').title()
        surname = input('Введите фамилию: ').title()
        tlp = (surname, name)
        for key in phonebook_dict:
            if tlp == key:
                print('Такой человек уже есть в словаре!')
                break
        else:
            phonebook_dict[tlp] = int(input('Введите номер телефона: '))
        print()
        for i_key, i_val in phonebook_dict.items():
            print(i_key[0], i_key[1], i_val)
    elif action == 'поиск':
        coincidence = False
        surname = input('\nВведите фамилию: ').title()
        for j_person in phonebook_dict:
            if surname in j_person:
                coincidence = True
                print(j_person[1], phonebook_dict[j_person])
        if not coincidence:
            print('Нет такого человека в словаре!')
    else:
        print('Ошибка! Неверный ввод!')

# зачет!
