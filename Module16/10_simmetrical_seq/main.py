def palindrome(lst):
    for i in range(len(lst)):
        if lst[i:] == lst[i:][::-1]:
            return True
        else:
            return False


numbers = int(input('\nКол-во чисел: '))
nums_list = []
conversely = []
for _ in range(numbers):
    num = int(input('Число: '))
    nums_list.append(num)
print('\nПоследовательность:', nums_list)

for i_num in range(len(nums_list)):
    new_nums_list = []
    for i_elem in range(i_num, len(nums_list)):
        new_nums_list.append(nums_list[i_elem])
    if palindrome(new_nums_list):
        for i_con in range(0, i_num):
            conversely.append(nums_list[i_con])
        conversely.reverse()
        break
print('Нужно приписать чисел:', len(conversely))
print('Сами числа:', conversely)

# зачет!
