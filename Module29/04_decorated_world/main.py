from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_expand: Callable) -> Callable:
    """ Декоратор, который разрешает другому декоратору принимать произвольные аргументы """
    def decorator_creator(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_expand(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_creator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор. Шаблон. """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Арги и кварги переданные в декоратор:', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачет!
