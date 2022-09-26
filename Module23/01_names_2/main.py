def record(elem):
    with open('errors.log', 'a', encoding='utf-8') as errors:
        errors.write(str(f'{elem}\n'))
    print(error)


sym_sum = 0
try:
    with open('people.txt', 'r', encoding='utf-8') as file_people:
        for line_count, i_line in enumerate(file_people, 1):
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                error = Exception(f'Длина {line_count} строки меньше трёх символов')
                record(error)
            sym_sum += length
        raise error
except FileExistsError:
    error = 'Файл не найден.'
    record(error)
except NameError:
    error = 'Нет имен пользователей, у которых символов меньше трёх'
    record(error)
finally:
    print('Найденная сумма символов:', sym_sum)

# зачет!
