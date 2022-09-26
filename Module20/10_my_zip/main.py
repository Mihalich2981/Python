line = 'abcd'
nums_tpl = (10, 20, 30, 40)
print(f'\nСтрока: {line}\nКортеж чисел: {nums_tpl}')
generator = ((line[i_elem], nums_tpl[i_elem]) for i_elem in range(min(len(line), len(nums_tpl))))
print(f'\nРезультат:\n{generator}')
for j_elem in generator:
    print(j_elem)

# зачет!
