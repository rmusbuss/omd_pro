import asyncio


async def magic_func() -> int:
    return 42


async def fix_this_code() -> int:
    # С этой функцией что-то не так, необходимо разобраться что именно и починить её.

    # способ 1
    # return await magic_func()

    # способ 2
    coroutine = magic_func()
    task = asyncio.create_task(coroutine)
    return await task
