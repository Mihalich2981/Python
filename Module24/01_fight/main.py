import random


class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        print(f'Создан воин {name} со здоровьем в {health} очков')

    def hit(self):
        print(f'\nАтаковал воин {self.name}.', end='')

    def defense(self):
        self.health -= 20
        if self.health > 0:
            print(f'\nУ воина {self.name} осталось {self.health} очков здоровья')
        else:
            print(f' И он ПОБЕДИЛ!')


warrior_1 = Warrior('Михаил', 100)
warrior_2 = Warrior('Александр', 100)

while (warrior_1.health > 0) and (warrior_2.health > 0):
    attack = random.randint(1, 2)
    if attack == 1:
        warrior_1.hit()
        warrior_2.defense()
    else:
        warrior_2.hit()
        warrior_1.defense()

# зачет!
