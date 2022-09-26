def summa_file(file):
    summa = 0
    for i_line in file:
        print(i_line, end='')
        # TODO проверь ещё раз с i_line.split() вместо list(i_line)
        # Проверил! Сумма 30, если нет пробела. Я проверял сразу эти варианты: i_line.split() и list(i_line.split()).
        num = sum([int(i_num) if i_num.isdigit() else 0 for i_num in list(i_line)])
        summa += num
    return summa


file_1 = open('numbers.txt', 'r', encoding='utf-8')
print('Содержимое файла numbers.txt:')
result = summa_file(file_1)
file_1.close()
print()
file_2 = open('answer.txt', 'w', encoding='utf-8')
print('\nСодержимое файла answer.txt')
file_2.write(str(result))
file_2.close()
file_2 = open('answer.txt', 'r', encoding='utf-8')
data = file_2.read()
print(data)
file_2.close()
