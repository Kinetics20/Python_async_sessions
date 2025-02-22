import asyncio


from util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finished')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed > 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print('Cancelled')


asyncio.run(main())

