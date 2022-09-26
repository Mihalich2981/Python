def histogram(string, sym_dict):
    for sym in string:
        if sym.isalpha():
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    return sym_dict


file = open('text.txt', 'r', encoding='utf-8')
print('\nСодержимое файла text.txt:')
num_sym = {}
for i_line in file:
    print(i_line)
    num_sym = histogram(i_line.lower(), num_sym)
file.close()
sorted_num = dict(sorted(sorted(num_sym.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True))
new_file = open('analysis.txt', 'a', encoding='utf-8')
summa = sum(sorted_num.values())
for key, val in sorted_num.items():
    new_file.write(f'{key} {round(val/summa, 3)}\n')
print('\nСодержимое файла analysis.txt:')
new_file = open('analysis.txt', 'r', encoding='utf8')
new_data = new_file.read()
print(new_data)
file.close()

# зачет!
