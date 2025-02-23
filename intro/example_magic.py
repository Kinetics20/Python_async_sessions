import asyncio

from util import delay


async def main()-> None:
    print('1')
    result = asyncio.create_task(delay(2))
    await delay(3)
    print('2')

asyncio.run(main())
