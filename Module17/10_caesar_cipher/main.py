def caesar_cipher(text, code):
    new_text = ''
    lst = [(alpha[(alpha.index(sym) + code) % len(alpha)] if sym != ' ' else ' ') for sym in text]
    for i_sym in lst:
        new_text += i_sym
    return new_text


alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
messages = input('\nВведите сообщение: ')
shift = int(input('Введите сдвиг: '))

code_sms = caesar_cipher(messages, shift)
print('Зашифрованное сообщение:', code_sms)

# зачет!
