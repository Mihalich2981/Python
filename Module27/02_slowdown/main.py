from typing import Callable, Any
import functools
import time


def waiting(func: Callable) -> Callable:
    """
    Декаратор, который перед выполнением
    декорируемой функции ждёт несколько секунд
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('\nИдет анализ данных...')
        time.sleep(5)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@waiting
def get_data() -> None:
    print('Анализ завершён. Продолжайте работать.')


get_data()

# зачет!
