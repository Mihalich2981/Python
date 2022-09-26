num = int(input('\nВведите максимальное число: '))
plenty = {i_num for i_num in range(1, num + 1)}
while True:
    nums_str = input('\nНужное число есть среди вот этих чисел: ').title().split()
    if nums_str[0] == 'Помогите!':
        print('Артём мог загадать следующие числа:', end=' ')
        for j_num in plenty:
            print(j_num, end=' ')
        break
    else:
        nums = {int(i_sym) for i_sym in nums_str}
        answer = input('Ответ Артёма: ').title()
        if answer == 'Да':
            plenty.intersection_update(nums)
        elif answer == 'Нет':
            plenty.difference_update(nums)
        else:
            print('Ошибка! Ответ Артёма: "Да" или "Нет"')

# зачет!
