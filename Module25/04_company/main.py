from random import randint, choice

names_lst = ['Алексей', 'Женя', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим', 'Миша', 'Коля']
surname_lst = ['Орлов', 'Сидоров', 'Иванов', 'Панин', 'Петров', 'Ерин', 'Юдин', 'Козлов', 'Рябов']


def generate_person():
    """
    Функция рандомно выбирающая имя, фамилию и возраст
    :return: name (str), surname (str), age (int)
    """
    name = choice(names_lst)
    names_lst.remove(name)
    surname = choice(surname_lst)
    surname_lst.remove(surname)
    age = randint(20, 50)
    return name, surname, age


class Person:
    """
    Базовый класс, описывающий человека
    Args:
        name (str) - передаётся имя человека
        surname (str) - передаётся фамилия человека
        age (int) - передаётся возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'\nЯ - {self.__name} {self.__surname}.\tМне - {self.__age}.'


class Employee(Person):
    """
    Класс Работник , Родитель: Person
    Args:
        name (str) - передаётся имя человека
        surname (str) - передаётся фамилия человека
        age (int) - передаётся возраст человека
    Attributes:
        wages (int) - заработная плата человека
    """
    wages = 0

    def calc_salary(self):
        """
        Метод расчета заработной платы
        :return:  wages (int)
        """
        return self.wages

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {self.calc_salary()} руб.'


class Manager(Employee):
    """
    Класс Manager , Родитель: Employee
    Args:
        name (str) - передаётся имя человека
        surname (str) - передаётся фамилия человека
        age (int) - передаётся возраст человека
    Attributes:
        wages (int) - заработная плата человека
   """
    wages = 13000

    def __str__(self):
        return super().__str__() + f' Специальность: Менеджер.'


class Agent(Employee):
    """
    Класс Agent , Родитель: Employee
    Args:
        name (str) - передаётся имя человека
        surname (str) - передаётся фамилия человека
        age (int) - передаётся возраст человека
        sales (int) - объема продаж
    Attributes:
        wages (int) - заработная плата человека
    """
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.wages = 5000 + .05 * sales

    def __str__(self):
        return super().__str__() + f' Специальность: Агент.'


class Worker(Employee):
    """
    Класс Agent , Родитель: Employee
    Args:
        name (str) - передаётся имя человека
        surname (str) - передаётся фамилия человека
        age (int) - передаётся возраст человека
        hours (int) - число отработанных часов
    Attributes:
        wages (int) - заработная плата человека
    """
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.wages = 100 * hours

    def __str__(self):
        return super().__str__() + f' Специальность: Работник.'


employees = []
for _ in range(3):
    employees.append(Manager(*generate_person()))
for _ in range(3):
    employees.append(Agent(*generate_person(), sales=randint(2000, 10000)))
for _ in range(3):
    employees.append(Worker(*generate_person(), hours=randint(25, 50)))

for i_emp in employees:
    print(i_emp)

# зачет!
