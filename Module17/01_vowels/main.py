text = input('\nВведите текст: ').lower()
vowels = 'аоеёуэыяюи'
lst_vowels = [buk for buk in text if buk in vowels]
print('\nСписок гласных букв:', lst_vowels)
print('Длина списка:', len(lst_vowels))

# зачет!
