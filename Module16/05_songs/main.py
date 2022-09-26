violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs = int(input('\nСколько песен выбрать? '))
summa = 0

for i_num in range(songs):
    print('Название', i_num + 1, 'песни:', end=' ')
    song = input()
    for item, cost in violator_songs:
        if item == song:
            summa += cost
            break
print('\nОбщее время звучания песен:', round(summa, 2), 'минут')

# зачет!
