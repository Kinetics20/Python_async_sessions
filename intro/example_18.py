import asyncio

from util import delay


def call_later() -> None:
    print("Calling in future")

async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
    await delay(2)

asyncio.run(main())