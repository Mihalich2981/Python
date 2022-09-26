def correct_input(numbers):
    correct = False
    for i_num in numbers:
        if i_num.isdigit():
            if int(i_num) > 255:
                print(i_num, 'превышает 255')
                break
            elif int(i_num) < 0:
                print(i_num, '- отрицательное число')
                break
        else:
            print(i_num, '- не целое число')
            break
    else:
        print('IP-адрес корректен')
        correct = True
    return correct


while True:
    address = input('\nВведите IP: ').split('.')
    if len(list(address)) != 4:
        print('Адрес - это четыре целых числа, разделенные точками')
    else:
        if correct_input(address):
            break

# зачет!
