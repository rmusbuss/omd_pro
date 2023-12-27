import asyncio
from dataclasses import dataclass
from typing import Awaitable, Iterable
from operator import attrgetter


@dataclass
class Ticket:
    number: int
    key: str


def get_object_names(iterable: Iterable, attr_name: str) -> list:
    attrgetter_attr = attrgetter(attr_name)
    return list(map(attrgetter_attr, iterable))


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    # YOUR CODE GOES HERE
    
    # способ 1
    # tasks = [asyncio.create_task(coro) for coro in coros]
    # results = [await task for task in tasks]
    # sorted_results = sorted(results, key=attrgetter('number'))
    # final_results = get_object_names(sorted_results, 'key')
    
    # способ 2
    results = await asyncio.gather(*coros)
    sorted_results = sorted(results, key=attrgetter('number'))
    final_results = get_object_names(sorted_results, 'key')
    
    return ''.join(final_results)
