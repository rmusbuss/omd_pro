from dataclasses import dataclass
from operator import itemgetter, attrgetter
from typing import Iterable


@dataclass
class User:
    name: str
    age: int


def get_names(iterable: Iterable, item_name: str) -> list:
    itemgetter_item = itemgetter(item_name)
    return list(map(itemgetter_item, iterable))


def get_object_names(iterable: Iterable, attr_name: str) -> list:
    attrgetter_attr = attrgetter(attr_name)
    return list(map(attrgetter_attr, iterable))


users_objects = [User(name="Paul", age=28), User(name="Liz", age=18)]

users = [
    {"name": "Paul", "age": 28},
    {"name": "Liz", "age": 18},
]

if __name__ == "__main__":
    assert list(get_names(users, "name")) == ["Paul", "Liz"]
    assert list(get_object_names(users, "name")) == ["Paul", "Liz"]
