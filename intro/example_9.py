import asyncio


from util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=1)
        print(result)
    except asyncio.TimeoutError:

        print("Timed took longer that 1 second")
        print(long_task.cancelled())
        result = await long_task
        print(result)



asyncio.run(main())

