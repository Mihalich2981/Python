def fib(number):
    if number < 1:
        return 0
    elif number == 1:
        return 1
    return fib(number - 1) + fib(number - 2)


num = int(input('\nВведите позицию числа в ряде Фибоначчи: '))
print(f'\nЧисло: {fib(num)}')

# зачет!
