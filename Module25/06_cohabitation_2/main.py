from random import randint


class Person:
    sum_food = 0
    sum_fur = 0
    sun_money = 0

    def __init__(self, name, house, satiety=30, bliss=100):
        self.name = name
        self.satiety = satiety
        self.bliss = bliss
        self.house = house

    def __str__(self):
        return f'{self.name} - сытость: {self.satiety}, счастье: {self.bliss}.'

    def eat(self):
        if self.satiety <= 10:
            self.satiety += 30
            self.sum_food += 30
            self.house.food -= 30
        else:
            self.satiety += 10
            self.sum_food += 10
            self.house.food -= 10
        return print(f'{self.name} ест!')

    def petting_cat(self):
        self.satiety -= 10
        self.bliss += 5
        return print(f'{self.name} гладит питомца!')

    def get_sum_food(self):
        return self.sum_food

    def get_sum_fur(self):
        return self.sum_fur

    def get_sun_money(self):
        return self.sun_money


class Father(Person):

    def work(self):
        self.satiety -= 10
        self.house.money += 150
        self.sun_money += 150
        return print(f'{self.name} работает!')

    def play(self):
        self.satiety -= 10
        self.bliss += 20
        return print(f'{self.name} играет!')

    def action(self):
        if self.house.dirt > 90:
            self.bliss -= 10
        if self.satiety < 0:
            print(f'К сожалению, {self.name} умирает с голоду!')
            return True
        elif self.bliss < 10:
            print(f'К сожалению, {self.name} умирает от депрессии!')
            return True
        else:
            if self.satiety <= 10:
                self.eat()
            elif self.bliss <= 15:
                self.petting_cat()
            elif self.house.money <= 80:
                self.work()
            else:
                nums = randint(1, 10)
                if nums < 6:
                    self.work()
                elif nums < 9:
                    self.eat()
                elif nums == 9:
                    self.play()
                else:
                    self.petting_cat()


class Mother(Person):

    def buy_groceries(self):
        self.satiety -= 10
        self.house.money -= 80
        if (self.house.food <= 20) and (self.house.cat_food <= 10):
            self.house.food += 50
            self.house.cat_food += 30
            return print(f'{self.name} идёт за продуктами и кормом!')
        elif self.house.cat_food <= 10:
            self.house.cat_food += 80
            return print(f'{self.name} идёт за кормом!')
        else:
            self.house.food += 80
            return print(f'{self.name} идёт за продуктами!')

    def buy_fur_coat(self):
        self.satiety -= 10
        self.bliss += 60
        self.house.money -= 350
        self. sum_fur += 1
        return print(f'Счастливая {self.name} покупает шубу!')

    def cleaning(self):
        self.satiety -= 10
        self.house.dirt -= 100
        return print(f'{self.name} делает уборку!')

    def action(self):
        if self.house.dirt > 90:
            self.bliss -= 10
        if self.satiety < 0:
            print(f'К сожалению, {self.name} умирает с голоду!')
            return True
        elif self.bliss < 10:
            print(f'К сожалению, {self.name} умирает от депрессии!')
            return True
        else:
            if self.satiety <= 10:
                self.eat()
            elif self.bliss <= 15:
                self.petting_cat()
            elif (self.house.food <= 20) or (self.house.cat_food <= 10):
                self.buy_groceries()
            elif self.house.dirt >= 100:
                self.cleaning()
            elif self.house.money >= 350:
                self.buy_fur_coat()
            else:
                nums = randint(1, 5)
                if nums < 4:
                    self.eat()
                elif nums == 4:
                    self.buy_groceries()
                else:
                    self.petting_cat()


class Child(Person):

    def play(self):
        self.satiety -= 10
        self.bliss += 10
        self.house.dirt -= 20
        return print(f'{self.name} играет и наводит бардак!')

    def action(self):
        if self.house.dirt > 90:
            self.bliss -= 10
        if self.satiety < 0:
            print(f'К сожалению, {self.name} умирает с голоду!')
            return True
        elif self.bliss < 10:
            print(f'К сожалению, {self.name} умирает от депрессии!')
            return True
        else:
            if self.satiety <= 10:
                self.eat()
            elif self.bliss <= 15:
                self.petting_cat()
            else:
                nums = randint(1, 3)
                if nums == 1:
                    self.eat()
                elif nums == 2:
                    self.play()
                else:
                    self.petting_cat()


class Cat:
    sum_food_cat = 0

    def __init__(self, name, house, satiety=30):
        self.name = name
        self.satiety = satiety
        self.house = house

    def __str__(self):
        return f'{self.name} - сытость: {self.satiety}.'

    def eat(self):
        if self.satiety <= 10:
            self.satiety += 20
            self.sum_food_cat += 20
            self.house.cat_food -= 10
        else:
            self.satiety += 10
            self.sum_food_cat += 10
            self.house.cat_food -= 5
        return print(f'{self.name} ест!')

    def sleep(self):
        self.satiety -= 10
        return print(f'{self.name} спит!')

    def tear_wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 5
        return print(f'Засранец {self.name} дерёт обои!')

    def action_cat(self):
        if self.satiety < 0:
            print(f'К сожалению, {self.name} умирает с голоду!')
            return True
        else:
            if self.satiety < 10:
                self.eat()
            else:
                nums = randint(1, 3)
                if nums == 1:
                    self.tear_wallpaper()
                elif nums == 2:
                    self.eat()
                else:
                    self.sleep()

    def get_sum_food_cat(self):
        return self.sum_food_cat


class House:

    def __init__(self, money=100, food=50, cat_food=30, dirt=0):
        self.money = money
        self.food = food
        self.cat_food = cat_food
        self.dirt = dirt

    def __str__(self):
        return f'\nДенег в тумбочке: {self.money}, уровень грязи: {self.dirt}' \
               f'\nЕды в холодильнике: {self.food}, для животных: {self.cat_food}.'

    def pollution(self):
        self.dirt += 5
        if self.dirt > 90:
            print(f'В доме грязно: {self.dirt}')
        return self.dirt


home = House()
father = Father('Папа Миша', home)
mother = Mother('Мама Таня', home)
child = Child('Диана', home)
cat_1 = Cat('Хулимяу', home)
cat_2 = Cat('Идинах', home)
cat_3 = Cat('Шкура', home)

for i_day in range(365):
    print(f'\nДень: {i_day+1}')
    print(home)
    print(father)
    print(mother)
    print(child)
    print(cat_1)
    print(cat_2)
    print(cat_3)
    home.pollution()
    print()
    if father.action() or mother.action() or child.action()\
            or cat_1.action_cat() or cat_2.action_cat() or cat_3.action_cat():
        print('Всё плохо!')
        break
else:
    print('Выжили!')

money_earned = father.get_sun_money()
food_people = child.get_sum_food()
food_animals = cat_1.get_sum_food_cat()
fur_purchased = mother.get_sum_fur()
print(f'\nПодведение итогов жизни за год:'
      f'\n1) Папа заработал: {money_earned} денег.'
      f'\n2) Мама купила: {fur_purchased} шуб.'
      f'\n3) Люди съели: {food_people} еды.'
      f'\n4) Животные съели: {food_animals} еды.'
      f'\nВсего съели: {food_people + food_animals} еды')

# зачет!
