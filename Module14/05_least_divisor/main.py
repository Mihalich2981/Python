
def smallest_divisor(num):
    import math
    half = int(math.sqrt(num))
    for var in range(2,  half + 1):
        if num % var == 0:
            break
    else:
        var = num
    return var

while True:
    number = int(input('Введите число: '))
    if number > 1:
        break

divisor = smallest_divisor(number)
print('\nНаименьший делитель, отличный от единицы:', divisor)
