from typing import List


strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]


results: List[tuple] = [(strings[elem], numbers[elem]) for elem in range(min(len(strings), len(numbers)))]
print(results)

# зачет!
