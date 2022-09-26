with open('calc.txt', 'r', encoding='utf-8') as file:
    print('\nСодержимое файла calc.txt')
    print(file.read())
with open('calc.txt', 'r', encoding='utf-8') as file:
    summa = 0
    print('\nСодержимое консоли:')
    for i_line in file:
        try:
            summa += eval(i_line)
        except (ArithmeticError, SyntaxError, NameError, TypeError):
            answer = input(f'Обнаружена ошибка в строке: {i_line[:-1]}   Хотите исправить? ').lower()
            if (answer == 'да') or (answer == 'yes'):
                new_line = input('Введите исправленную строку: ')
                summa += eval(new_line)
    print('\nСумма результатов:', summa)

# зачет!
