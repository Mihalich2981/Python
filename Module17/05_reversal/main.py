line = input('\nВведите строку : ').lower()
first = line.index('h')
nearest = line.rindex('h')
result = line[nearest - 1:first:-1]
print('Результат:', result)

# зачет!
