word = input('Введите слово: ')
word_list = list(word)
unique = 0
for letter in word_list:
    var = 0
    for i in word_list:
        if letter == i:
            var += 1
    if var < 2:
        unique += 1
print('Кол-во уникальных букв:', unique)

# зачет!
