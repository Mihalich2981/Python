from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декаратор, считающий и выводящий
    количество вызовов декорируемой функции”
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        wrapped_func.count += 1
        func(*args, **kwargs)
        print(f'Функция {func.__name__} - вызвана {wrapped_func.count} раз(а).')
    wrapped_func.count = 0
    return wrapped_func


@counter
def test() -> None:
    print('<Тут что-то происходит...>')


test()
test()
test()
test()
test()

# зачет!
