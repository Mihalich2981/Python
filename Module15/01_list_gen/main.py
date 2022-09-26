def odd(num):
    numbers = []
    for i in range(1, num + 1, 2):
        numbers.append(i)
    return numbers


while True:
    number = int(input('\nЦелое число: '))
    if number > 0:
        break

numbers = odd(number)

print('\nСписок нечетных чисел:', numbers)

# зачет!
