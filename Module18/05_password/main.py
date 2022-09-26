while True:
    password = input('\nПридумайте пароль: ')
    num = 0
    for i_sym in password:
        if i_sym in '0123456789':
            num += 1
    if len(password) < 7 or num < 3 or password.isalpha() or password.islower() or password.isupper():
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

# зачет!
