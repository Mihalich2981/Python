line = list(input('\nВведите строку: '))
symbol = line[0]
code = 1
code_line = []
for i_sym in line[1:]:
    if symbol == i_sym:
        code += 1
    else:
        code_line.append(symbol)
        code_line.append(str(code))
        symbol = i_sym
        code = 1
if line[:-1] != line[:-2]:
    code_line.append(symbol)
    code_line.append(str(code))
print('Закодированная строка:', ''.join(code_line))

# зачет!
