def lst_pairs(*args):
    return [tuple(elem[i] for elem in args) for i in range(min(map(len, args)))]


lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

print()
print(lst_pairs(lst_1, lst_2))

# зачет!
