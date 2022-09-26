from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """
    Декаратор, отвечающий за логирование функций.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        try:
            func(*args, **kwargs)
            return print(f'\nНазвание функции: "{func.__name__}"\nДокументация:{func.__doc__}')
        except Exception as error:
            error_content = f'Функция: "{func.__name__}", Ошибка: "{error}", Дата и время: "{datetime.datetime.now()}"\n'
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(error_content)
    return wrapped_func


@logging
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов,
    для каждого N от 1 до 10000,
    где 0 <= N <= 100
    Returns: сумма квадратов
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result


@logging
def perky(param: float) -> Any:
    """
    Функция деления на ноль
    Returns: результат деления
    """
    return param / 0


perky(28)
squares_sum()

# зачет!
