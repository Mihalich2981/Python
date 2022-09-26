def long_word(lst):
    maxi = ''
    for i_line in lst:
        if len(i_line) > len(maxi):
            maxi = i_line
    return maxi


text = input('\nВведите строку, содержащую пробелы: ').split()
max_word = long_word(text)
print('\nСамое длинное слово:', max_word)
print('Его длина', len(max_word), 'символов')

# зачет!
