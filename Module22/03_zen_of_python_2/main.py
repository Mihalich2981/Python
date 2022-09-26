import os


def histogram(string, sym_dict):
    for sym in string:
        if sym.isalpha():
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    return sym_dict


path = os.path.join('..', '02_zen_of_python', 'zen.txt')
file = open(path, 'r', encoding='utf-8')
line = 0
word = 0
num_sym = {}
for i_line in file:
    line += 1
    word += len(i_line.split())
    num_sym = histogram(i_line.lower(), num_sym)
file.close()
print(f'\nВ Дзене Питона: {line} строк и {word} слов.')
print(f'А также: {sum(num_sym.values())} буквы латинского алфавита.')
mini = min(num_sym.values())
letter = ''.join([key for key, val in num_sym.items() if val == mini])
print(f'Буква: {letter} - встречается в тексте наименьшее количество раз.')


# зачет!
