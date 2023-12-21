from typing import Iterable, Callable
from abc import ABC


class SeqABC(ABC):
    pass


class Seq(SeqABC):
    def __init__(self, iterable: Iterable):
        self.iterable = iterable.copy()
        self.original_type = type(iterable)

    def filter(self, func: Callable) -> SeqABC:
        self.iterable = filter(func, self.iterable)
        return self

    def map(self, func: Callable) -> SeqABC:
        self.iterable = map(func, self.iterable)
        return self

    def take(self, num: int) -> Iterable:
        return self.original_type(self.iterable)[:num]

    def __str__(self):
        return f"{self.iterable}"


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)

    assert res == [12, 14]
