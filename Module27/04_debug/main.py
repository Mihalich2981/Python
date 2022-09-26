from typing import Callable
import functools


def debug(func: Callable) -> Callable:
    """
    Декаратор, который при каждом вызове декорируемой функции
    выводит её имя (вместе со всеми передаваемыми аргументами)
    и затем какое значение она возвращает.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('\nВызывается {}({})'.format(
            func.__name__,
            ', '.join(
                list(f'"{arg}"' if isinstance(arg, str) else str(arg) for arg in args)
                + list(f'{i}="{j}"' if isinstance(j, str) else f'{i}={j}' for i, j in kwargs.items())
            )
        ))
        result = func(*args, **kwargs)
        print("'{}' вернула значение'{}'".format(func.__name__, result))
        print(result)
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачет!
