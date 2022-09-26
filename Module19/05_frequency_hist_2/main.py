def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def inverted_dictionary(dct):
    new_dct = dict()
    nums = set(dct.values())
    for num in nums:
        lst = []
        for sym in dct:
            if num == dct[sym]:
                lst.append(sym)
        new_dct[num] = lst
    return new_dct


text = input('\nВведите текст: ')
print('Оригинальный словарь частот:')
hist = histogram(text)

for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('\nИнвертированный словарь частот:')
inv_hist = inverted_dictionary(hist)

for j_sym in sorted(inv_hist.keys()):
    print(j_sym, ':', inv_hist[j_sym])

# зачет!
