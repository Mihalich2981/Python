file = input('\nНазвание файла: ')
symbol = list('@№$%^&*()')

for i_sym in range(len(symbol)):
    if file.startswith(symbol[i_sym]):
        print('Ошибка: название начинается на один из специальных символов')
        break
    elif not file.endswith(('.txt', '.docx')):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        break
    else:
        print('Файл назван верно.')
        break

# зачет!
