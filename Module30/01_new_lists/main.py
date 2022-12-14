from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

list_1: List[float] = list(map(lambda num: round(num ** 3, 3), floats))
print(list_1)
list_2: List[str] = list(filter(lambda name: len(name) >= 5, names))
print(list_2)
multiplication = reduce(lambda num_1, num_2: num_1 * num_2, numbers)
print(multiplication)

# зачет!
