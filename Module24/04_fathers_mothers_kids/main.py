import random


class Parent:

    def __init__(self, name, age, children=None):
        self.name = name
        self.age = age
        self.children = children

    def information(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.')

    def calm_child(self, child_name):
        print(f'{child_name} - плачет.')
        print(f'{self.name} успокоил(а) ребенка.')
        print(f'{child_name} успокоился(ась)!')

    def feed_baby(self, child_name):
        print(f'{child_name} - голоден(на).')
        print(f'{self.name} покормил(а) ребенка.')
        print(f'{child_name} сыт(а)!')


class Child:

    def __init__(self, name_child, age_child):
        self.name_child = name_child
        self.age_child = age_child
        self.calmness = random.choice([True, False])
        self.hunger = random.choice([True, False])


names_child = list(input('\nВведите имена детей семьи, через пробел: ').split())
p_f = Parent('Михаил', 40, names_child)
p_m = Parent('Татьяна', 36, names_child)

for i_name in names_child:
    while True:
        age_c = int(input('Введите возраст ребёнка: '))
        if age_c + 16 <= min(p_f.age, p_m.age):
            break
        else:
            print('Неверный возраст ребёнка! Попробуй ещё раз...')
    child = Child(i_name, age_c)
    if not child.calmness:
        random.choice([p_f, p_m]).calm_child(i_name)
        child.calmness = True
    if child.hunger:
        random.choice([p_f, p_m]).feed_baby(i_name)
        child.hunger = False

# зачет!
