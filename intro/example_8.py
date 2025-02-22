import asyncio


from util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(long_task, timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("Timed out")
        print(long_task.cancelled())



asyncio.run(main())

