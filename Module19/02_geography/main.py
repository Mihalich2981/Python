num_countries = int(input('\nКол-во стран: '))
cities = dict()

for i_num in range(num_countries):
    country = input(f'{i_num + 1} страна: ').split()
    for i_citi in range(1, len(country)):
        cities[country[i_citi]] = country[0]

for i_loc in range(3):
    citi = input(f'\n{i_loc + 1} город: ')
    if citi in cities:
        print('Город', citi, 'расположен в стране', cities[citi])
    else:
        print('По городу', citi, 'данных нет.')

# зачет!
