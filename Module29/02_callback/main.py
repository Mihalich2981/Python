from typing import Callable, Any
import functools
app = {}


def callback(key: str) -> Callable:
    """ Функция обратного вызова """
    def dec_callback(func: Callable) -> Callable:
        app[key] = func

        @functools.wraps(func)
        def wrapped_callback(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return wrapped_callback
    return dec_callback


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачет!
