from asyncio import Task, create_task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        coroutine = f()
        task = create_task(coroutine)
        return await task
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        task = create_task(f)
        return await f
    else:
        raise ValueError('invalid argument')
