import timeit


res_1: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('Вариант 1:', res_1)
res_2: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print('Вариант 2:', res_2)
res_3: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print('Вариант 3:', res_3)
res_4: float = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
print('Вариант 4:', res_4)

# зачет!
