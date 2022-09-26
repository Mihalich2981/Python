#Вариант 1 (с помощью итератора)

class QHofstadter:
    def __init__(self, s: list) -> None:
        self.s = s[:]

    def __next__(self) -> list:
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> iter:
        return self

    def current_state(self) -> list:
        return self.s


#Вариант 2 (с помощью генератора)

def hofstadter_generator(s):
    a = s[:]
    while True:
        try:
            q = a[-a[-1]] + a[-a[-2]]
            a.append(q)
            yield q
        except IndexError:
            return

# зачет!
