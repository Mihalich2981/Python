import math

def versa(num):
  num_versa = ''
  for var in num:
    num_versa = var + num_versa
  return num_versa

def generalization(num):
    integer = versa(str(math.floor(num)))
    fractional = math.floor(float(versa(str(num))))
    return float(integer + '.' + str(fractional))

first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
first = generalization(first)
print('\nПервое число наоборот:', first)
second = generalization(second)
print('Второе число наоборот:', second)
print('Сумма:', first + second)

# зачет!
