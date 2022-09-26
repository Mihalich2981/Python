import math

numbers = 10000

print('\nВариант 1')
prime = [2] + [num for num in range(3, numbers + 1, 2) if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))]
print(prime)

print('\nВариант 2') # Наиболее лучший и читаем
prime = range(2, numbers + 1)
for i in range(2, int(math.sqrt(numbers)) + 1):
    prime = list(filter(lambda x: x == i or x % i, prime))
print(prime)

# зачет!
