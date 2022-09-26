from random import randint, choice


class MyError(Exception):
    """Базовый класс для других исключений"""
    pass


class KillError(MyError):
    """Вызывается, когда убийство"""
    pass


class DrunkError(MyError):
    """Вызывается, когда пьянство"""
    pass


class CarCrashError(MyError):
    """Вызывается, когда автокатастрофа"""
    pass


class GluttonyError(MyError):
    """Вызывается, когда обжорство"""
    pass


class DepressionError(MyError):
    """Вызывается, когда депрессия"""
    pass


def one_day():
    error = [KillError('Убийство!'), DrunkError('Пьянство!'), CarCrashError('Автокатастрофа!'),
             GluttonyError('Обжорство!'), DepressionError('Депрессия!')]
    if randint(1, 10) == 1:
        try:
            raise choice(error)
        except Exception as error:
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(str(error) + '\n')
    return randint(1, 7)


# class MyError(Exception):
#     pass
#
#
# class KillError(MyError):
#     def __str__(self):
#         return f'Убийство'
#
#
# class DrunkError(MyError):
#     def __str__(self):
#         return f'Пьянство'
#
#
# class CarCrashError(MyError):
#     def __str__(self):
#         return f'Автокатастрофа'
#
#
# class GluttonyError(MyError):
#     def __str__(self):
#         return f'Обжорство'
#
#
# class DepressionError(MyError):
#     def __str__(self):
#         return f'Депрессия'


karma = 0
while karma < 500:
    karma += one_day()

# зачет!
