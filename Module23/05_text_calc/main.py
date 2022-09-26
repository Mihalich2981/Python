with open('calc.txt', 'r', encoding='utf-8') as file:
    summa = 0
    print()
    for count, i_line in enumerate(file, 1):
        try:
            summa += eval(i_line)
        except Exception as e:
            print(f'{e} в {count} строке')
    print('\nСумма результатов:', summa)

# зачет!
