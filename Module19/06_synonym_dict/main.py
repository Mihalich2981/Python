# Вариант 1
nums = int(input('\nВведите количество пар слов: '))
synonyms = dict()
log = False
for i_num in range(nums):
    word_1, word_2 = input(f'{i_num + 1} пара: ').title().split(' - ')
    synonyms[word_1] = word_2
while True:
    word = input('\nВведите слово: ').title()
    for i_sym in synonyms:
        if synonyms[i_sym] == word:
            print('Синоним:', i_sym)
            log = True
            break
    if log:
        break
    elif synonyms.get(word):
        print('Синоним:', synonyms[word])
        break
    else:
        print('Такого слова в словаре нет.')


# Вариант 2 (улучшенная версия)
nums = int(input('\nВведите количество пар слов: '))
synonyms = dict()
inv_synonyms = dict()

for i_num in range(nums):
    word_1, word_2 = input(f'{i_num + 1} пара: ').title().split(' - ')
    synonyms[word_1] = word_2
    inv_synonyms[word_2] = word_1

while True:
    word = input('\nВведите слово: ').title()
    if inv_synonyms.get(word):
        print('Синоним:', inv_synonyms[word])
        break
    elif synonyms.get(word):
        print('Синоним:', synonyms[word])
        break
    else:
        print('Такого слова в словаре нет.')

# зачет!
