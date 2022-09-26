

def similar(num):
    number = num % 10
    num //= 10
    summa = 0
    while num > 0:
        var = num % 10
        if number == var:
            summa += 1
            number = var
        num //= 10
    return summa


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print('\nГода от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
for year in range(first_year, second_year + 1):
    summa = similar(year)
    if summa == 2:
        print(year)

# зачет!
