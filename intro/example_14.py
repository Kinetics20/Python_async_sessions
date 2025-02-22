import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    task_three = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await task_three


asyncio.run(main())