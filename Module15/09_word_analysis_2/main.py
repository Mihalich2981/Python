word = input('\nВведите слово: ')
word_list = list(word)
length = len(word_list)
for i in range(int(length / 2)):
    if word_list[i] != word_list[length - 1 - i]:
        print('\nСлово не является палиндромом')
        break
else:
    print('\nСлово является палиндромом')

# зачет!
