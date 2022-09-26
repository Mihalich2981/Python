import random

squad_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
squad_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
champion = [(squad_1[i] if squad_1[i] > squad_2[i] else squad_2[i]) for i in range(20)]

print('\nПервая команда:', squad_1)
print('Вторая команда:', squad_2)
print('\nПобедители тура:', champion)


# зачет!