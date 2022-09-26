import random


class TicTacToe:
    def __init__(self):
        self.board = list(range(1, 10))
        self.human = None
        self.comp = None

    def draw_board(self):
        print('-' * 13)
        for i in range(3):
            print(f'| {self.board[0+i*3]} | {self.board[1+i*3]} | {self.board[2+i*3]} |')
            print('-' * 13)

    def chips(self):
        while True:
            self.human = input('\nЕсли хотите первым ходить, то выберете - Х, иначе - О: ').upper()
            if self.human == 'X':
                print('Окей, ты играешь крестиками и ходишь первый!')
                self.comp = 'O'
                return True
            elif self.human == 'O' or self.human == '0':
                print('Окей, ты играешь ноликами и ходишь вторым!')
                self.comp = 'X'
                return False
            else:
                print('Что-то не то выбрал! Попробуй ещё раз...')

    def my_move(self):
        while True:
            cell_num = random.randint(1, 9)
            if str(self.board[cell_num - 1]) not in 'XO':
                self.board[cell_num - 1] = self.comp
                break
        print(f'\nМой ход!\nПоставим {self.comp} в клетку {cell_num}')

    def your_move(self):
        while True:
            cell_num = input(f'\nТвой ход!\nКуда поставим {self.human} (от 1 до 9)? ')
            try:
                cell_num = int(cell_num)
            except ValueError:
                print('Некорректный ввод. Уверен, что ввел число?')
                continue
            if 1 <= cell_num <= 9:
                if str(self.board[cell_num - 1]) not in 'XO':
                    self.board[cell_num - 1] = self.human
                    break
                else:
                    print('Эта клетка занята! Выбери другую.')
            else:
                print('Число вне диапазона! Введи число от 1 до 9.')

    def victory(self):
        winning_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in winning_lines:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                if self.board[each[0]] == self.human:
                    print('\n***ПОБЕДА!***')
                else:
                    print('\n--Проиграл!--')
                self.draw_board()
                return True
        return False

    def game_progress(self):
        if self.chips():
            count = 1
        else:
            count = 2
        while count != 11:
            if count % 2 == 0:
                self.my_move()
            else:
                self.your_move()
            count += 1
            self.draw_board()
            if count > 5:
                if self.victory():
                    break
        else:
            print('\n=== Ничья! ===')
            self.draw_board()

    def start(self):
        print('\n', '*' * 5, 'Игра Крестики-Нолики', '*' * 5, '\n')
        self.draw_board()
        self.game_progress()
        print('\n', '-' * 5, 'Игра окончена!', '-' * 5, '\n')


game = TicTacToe()
game.start()

# зачет!
