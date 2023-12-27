import abc
import asyncio
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime as dt

class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model
        self._executor = ThreadPoolExecutor(max_workers=3)
    
#     async def process_task(self, executor: ThreadPoolExecutor):
#         print(f'{dt.now()}: task started')
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(executor, self._model.compute)
#         print(f'{dt.now()}: task finished')
        
    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.
        #
        # YOU CODE GOES HERE
#         with self._executor as executor:
#             asyncio.create_task(self.process_task(executor))
#         task = asyncio.create_task(self.process_task(self._executor))
#         await task
        print(f'{dt.now()}: task started')
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self._executor, self._model.compute)
        print(f'{dt.now()}: task finished')