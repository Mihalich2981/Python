def summa(*args):
    def flatten(lst):
        result = []
        for elem in lst:
            if isinstance(elem, int):
                result.append(elem)
            else:
                result.extend(flatten(elem))
        return result
    return sum(flatten(args))


print('Ответ:', summa([[1, 2, [3]], [1], 3]))
print('Ответ:', summa(1, 2, 3, 4, 5))

# зачет!
