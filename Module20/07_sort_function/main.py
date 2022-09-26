def fun_sort(tpl):
    for i_val in tpl:
        const = int(i_val)
        if const != i_val:
            return tpl
    lst = list(tpl)
    lst.sort()
    return tuple(lst)


# Пример 1
tpl_1 = (8, 2, 3, 9, 6, 5, 1)
# Пример 2
tpl_2 = (6, 2, 3.14, 3, 8, 5)

print(tpl_1, tpl_2)
print(fun_sort(tpl_1), fun_sort(tpl_2))

# зачет!
