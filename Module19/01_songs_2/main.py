violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num = int(input('\nСколько песен выбрать? '))
time = 0
for i_num in range(1, num + 1):
    name = input(f'Название {i_num} песни: ')
    if not violator_songs.get(name):
        print('Нет такой песни в этом альбоме')
    else:
        time += violator_songs[name]
print('\nОбщее время звучания песен:', round(time, 2), 'минут')

# зачет!
