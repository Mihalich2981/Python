def palindrome(string):
    pal_dict = dict()
    count = 0
    for i_sym in string:
        pal_dict[i_sym] = pal_dict.get(i_sym, 0) + 1
    for i_num in pal_dict.values():
        if i_num % 2 != 0:
            count += 1
    return count <= 1


line = input('\nВведите строку: ')
if palindrome(line):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

# зачет!
