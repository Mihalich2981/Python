import math

def hypotenuse(x, y):
    return math.sqrt(x ** 2 + y ** 2)

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
d = hypotenuse(x, y)
if d <= r:
    print('\nМонетка где-то рядом')
else:
    print('\nМонетки в области нет')

# зачет!
