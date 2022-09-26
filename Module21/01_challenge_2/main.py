def sequence(number):
    if number != 1:
        sequence(number - 1)
    return print(number, end=' ')


num = int(input('\nВведите число: '))
sequence(num)
print()

# зачет!
