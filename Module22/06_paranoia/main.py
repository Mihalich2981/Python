alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_cipher(text, code):
    lst = [(alpha[(alpha.index(sym) + code) % len(alpha)] if sym.isalpha() else sym) for sym in text]
    new_text = [i_sym for i_sym in lst]
    return ''.join(new_text)


file = open('text.txt', 'r', encoding='utf-8')
print('\nСодержимое файла text.txt:')
for count, i_line in enumerate(file, 1):
    print(i_line, end='')
    text_code = caesar_cipher(i_line, count)
    new_file = open('cipher_text.txt', 'a', encoding='utf8')
    new_file.write(text_code)
    new_file.close()
file.close()
print('\n\nСодержимое файла cipher_text.txt:')
new_file = open('cipher_text.txt', 'r', encoding='utf8')
new_data = new_file.read()
print(new_data)
file.close()

# зачет!
