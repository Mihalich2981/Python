families = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Иванов', 'Михаил'): 36,
    ('Иванова', 'Татьяна'): 33,
    ('Иванова', 'Алёна'): 11
}

surname = input('\nВведите фамилию: ').title()
coincidence = False
for i_key, i_val in families.items():

    # Вариант 1
    # dif = abs(len(i_key[0]) - len(surname))
    # mx = max(i_key[0], surname)
    # mn = min(i_key[0], surname)
    # if (mx == mn) or (mx[:-dif] == mn) and (dif < 2):
    #     coincidence = True
    #     print(i_key[0], i_key[1], i_val)

    # Вариант 2
    string = i_key[0]
    if string.startswith(surname):
        coincidence = True
        print(i_key[0], i_key[1], i_val)
if not coincidence:
    print('Нет таких в базе данных')

# зачет!
