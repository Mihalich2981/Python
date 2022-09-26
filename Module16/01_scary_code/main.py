a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
k = a.count(5)
for _ in range(k):
    a.remove(5)
print('\nКол-во цифр 5 при первом объединении:', k)
a.extend(c)
k = a.count(3)
print('\nКол-во цифр 3 при втором объединении:', k)
print('\nИтоговый список:', a)

# зачет!
