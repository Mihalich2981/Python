import functools


def singleton(cls):
    """ Декоратор, который превращает класс в одноэлементный,
    то есть будет сохранён только первый инстанс """
    @functools.wraps(cls)
    def singleton_wrapper(*args, **kwargs):
        if not singleton_wrapper.inst:
            singleton_wrapper.inst = cls(*args, **kwargs)
        return singleton_wrapper.inst
    singleton_wrapper.inst = None
    return singleton_wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# зачет!
