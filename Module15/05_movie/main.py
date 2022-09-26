films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_movies = []
film = ''
while True:
    film = input('\nВведите название фильма или "end": ')
    if film.lower() == 'end':
        print('\nДо свидания!')
        break
    for i in films:
        if film.lower() == i.lower():
            favorite_movies.append(i)
            print('\nДобавлено:', favorite_movies, 'Продолжите?')
            break
    else:
        print('\nВы ошиблись! Нет такого фильма в списке.')
print('\nВесь список любимых фильмов:', favorite_movies)

# зачет!
