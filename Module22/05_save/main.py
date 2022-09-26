import os


def existing_path(lst):
    path = os.path.abspath(os.path.sep)
    for i_folder in lst:
        path = os.path.join(path, i_folder)
        if not os.path.exists(path):
            print(f'Папки {i_folder} - не существует. Попробуйте заново!')
            path = 0
            break
    return path


def writing_file(path, text):
    if os.path.exists(path):
        answer = input('Вы действительно хотите перезаписать файл? ').lower()
        if (answer == 'да') or (answer == 'yes'):
            file_record = open(path, 'w')
            file_record.write(text)
            file_record.close()
            print('Файл успешно перезаписан!')
        elif (answer == 'нет') or (answer == 'no'):
            print('Файл остался без изменений!')
        else:
            print('Ответ непонятен. Попробуйте заново!')
    else:
        file_record = open(path, 'w')
        file_record.write(text)
        file_record.close()
        print('Файл успешно сохранён!')


line = input('\nВведите строку: ')
while True:
    folders_list = list(input('\nКуда хотите сохранить документ? '
                              'Введите последовательность папок (через пробел):\n').split())
    path_folders = existing_path(folders_list)
    if path_folders:
        break
name_file = input('\nВведите имя файла: ')
path_file = os.path.join(path_folders, name_file)
writing_file(path_file, line)

file = open(path_file, 'r')
data = file.read()
print('\nСодержимое файла:', data)
file.close()

# зачет!
