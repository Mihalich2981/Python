def max_num(num, nums_list):
    maxi = num
    for var in nums_list:
        if maxi <= var:
            maxi = var
    return maxi


number_cards = int(input('\nКол-во видеокарт: '))
video_cards = []
new_video_cards = []

for i in range(1, number_cards + 1):
    print(i, 'Видеокарта:', end=' ')
    num_card = int(input())
    video_cards.append(num_card)

print('\nСтарый список видеокарт:', video_cards)

maximum = max_num(num_card, video_cards)

# Либо так
# for i in video_cards:
#     if i != maximum:
#         new_video_cards.append(i)
# video_cards = new_video_cards


# Либо вот так
for i in video_cards:
    if i == maximum:
        video_cards.remove(i)
print('Новый список видеокарт:', video_cards)

# А как по-другому?
#  ну если ты удаляешь по значению, то можно посчитать, сколько раз 
#  встречается данный номер в списке и столько раз в цикле удалить её с помощью remove(). 
#  Но и твое решение верное, по сложности они можно сказать одинаковые
# зачет!
