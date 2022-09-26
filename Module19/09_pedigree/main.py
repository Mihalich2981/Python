nums_people = int(input('\nВведите количество человек: '))
couples_dict = dict()
names_dict = dict()

for i_num in range(1, nums_people):
    # тут молодец
    name_desc, parent_name = input(f'{i_num} пара: ').title().split()
    couples_dict[name_desc] = parent_name
    names_dict[name_desc] = 0
    names_dict[parent_name] = 0

for i_coup in couples_dict:
    var = i_coup
    while var in couples_dict:
        var = couples_dict[var]
        names_dict[i_coup] += 1

print('\n“Высота” каждого члена семьи:')
for i_name in sorted(names_dict):
    print(i_name, names_dict[i_name])

# зачет!
