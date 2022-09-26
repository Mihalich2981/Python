import random


class Players:
    def __init__(self):
        self.my_score = 0
        self.bot_score = 0
        self.deck = BlackJack()

    def choice(self):
        self.deck.start()
        for _ in range(2):
            self.my_score = self.deck.random_card(self.my_score, False)
            self.bot_score = self.deck.random_card(self.bot_score, True)
        while True:

            choice = input('\nБудете брать карту? (y/n) ').lower()
            if choice == 'y':
                self.my_score = self.deck.random_card(self.my_score, False)
                if self.bot_score < 19 and self.my_score <= 21:
                    self.bot_score = self.deck.random_card(self.bot_score, True)
                if self.my_score > 21 or self.bot_score == 21:
                    print('Извините, но вы проиграли!')
                    break
                elif self.my_score == 21 and self.bot_score == 21:
                    print('Ничья!')
                elif self.my_score == 21 or self.bot_score > 21:
                    print('Поздравляю, вы победили!')
                    break
            elif choice == 'n':
                if self.my_score > self.bot_score and self.bot_score < 19:
                    while self.bot_score < 19:
                        self.bot_score = self.deck.random_card(self.bot_score, True)
                if self.my_score < self.bot_score <= 21:
                    print(f'\nИзвините, но вы проиграли!'
                          f'\nУ Вас: {self.my_score} очков, у Крупье: {self.bot_score} очков.')
                else:
                    print(f'\nПоздравляю, вы победили!'
                          f'\nУ Вас: {self.my_score} очков, у Крупье: {self.bot_score} очков.')
                break
            else:
                print('Что-то не то ввели! Попробуй ещё раз.')


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4

    def start(self):
        random.shuffle(self.deck)

    def random_card(self, score, bot):
        current = self.deck.pop()
        if isinstance(current, int):
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        if not bot:
            print(f'У Вас: {current} - {score} очков.')
        else:
            print(f'У Крупье: {current} - {score} очков.')
        return score


print('\n               Игра в BlackJack началась')
print('-' * 65)
print('Карты имеют такие “ценовые” значения:')
print(' - от двойки до десятки — от 2 до 10 соответственно;')
print(' - у “картинок” (король, дама, валет) — 10;')
print(' - у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1).')
print('=' * 65)
game = Players()
game.choice()
print('\nДо новых встреч!')

# зачет!
