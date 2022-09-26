from typing import Callable, Any
import functools
user_permissions = ['admin']


def check_permission(ingress: str) -> Callable:
    def decorator_permission(func: Callable) -> Callable:
        """
        Декоратор, который проверяет
        есть ли у пользователя доступ к вызываемой функции
        """
        @functools.wraps(func)
        def wrapped_check(*args, **kwargs) -> Any:
            if ingress not in user_permissions:
                raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
            return func(*args, **kwargs)
        return wrapped_check
    return decorator_permission


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
