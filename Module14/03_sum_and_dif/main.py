def summ(num):
    summa = 0
    while num > 0:
        summa += num % 10
        num //= 10
    return summa


def quantity_num(num):
    quantity = 0
    while num > 0:
        quantity += 1
        num //= 10
    return quantity


while True:
    num = int(input('Введите число: '))
    if num > 0:
        break

summa = summ(num)
quantity = quantity_num(num)
print('\nСумма цифр:', summa)
print('Кол-во цифр в числе:', quantity)
print('Разность суммы и кол-ва цифр:', summa - quantity)

# зачет!
