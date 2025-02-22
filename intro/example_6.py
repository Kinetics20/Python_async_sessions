import asyncio

async def delay(delay_second: int) -> int:
    print(f'sleeping for {delay_second} seconds')
    await asyncio.sleep(delay_second)
    print(f'finishing for {delay_second} seconds')
    return delay_second

async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('Running other code while I am waiting')


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())