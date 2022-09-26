from random import randint


class Person:

    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety
        self.house = House()

    def fridge(self):
        self.house.food -= 1
        return f'еды {self.house.food}'

    def work(self):
        self.house.money += 1
        return f'денег {self.house.money}'

    def shop(self):
        self.house.food += 1
        self.house.money -= 1
        return f'еды {self.house.food}'

    def action(self):
        if self.satiety < 0:
            print(f'К сожалению, {self.name} помер с голоду!')
            return True
        else:
            number_cubes = randint(1, 6)
            if self.satiety < 20 or number_cubes == 2:
                if self.house.food < 10 and self.house.money == 0:
                    print(f'{self.name}, ест в холодильнике {self.fridge()}.')
                    print(f'А так как еды мало и нет денег, то он идет на работу.')
                    print(f'Зарабатывает {self.work()}, а затем в магазин.')
                    print(f'Покупает {self.shop()}. Его сытость {self.satiety}.')
                elif self.house.food < 10:
                    self.satiety += 1
                    print(f'{self.name}, ест в холодильнике {self.fridge()}.')
                    print(f'А так как еды мало, то он идет в магазин.')
                    print(f'Покупает {self.shop()}. Его сытость {self.satiety}.')
                else:
                    self.satiety += 1
                    print(f'{self.name}, ест в холодильнике {self.fridge()}. Его сытость {self.satiety}.')
            elif number_cubes == 1:
                self.satiety -= 1
                print(f'{self.name}, идет на работу.')
                print(f'Зарабатывает {self.work()}, Его сытость {self.satiety}.')
            else:
                self.satiety -= 1
                print(f'{self.name}, играет! Его сытость {self.satiety}.')
            return False


class House:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money


person_1 = Person('Артём')
person_2 = Person('Миша')

for i_day in range(365):
    print(f'\nДень: {i_day+1}')
    if person_1.action() or person_2.action():
        print('Всё плохо!')
        break
else:
    print('Выжили!')

# зачет!
