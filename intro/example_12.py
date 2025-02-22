import asyncio

from util import async_timed


@async_timed()
async def delay(delay_second: int) -> int:
    print(f'sleeping for {delay_second} seconds')
    await asyncio.sleep(delay_second)
    print(f'finishing for {delay_second} seconds')
    return delay_second

@async_timed()
async def main() -> None:
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())