import asyncio

from aiohttp import ClientSession, ClientTimeout


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as response:
        return response.status


async def main() -> None:
    session_timeout = ClientTimeout(total=30, connect=.1)

    async with ClientSession(timeout=session_timeout) as session:
        url = "http://127.0.0.1:8084"
        requests = [
            fetch_status(session, url),
            fetch_status(session, url),
            fetch_status(session, url)
        ]
        # statuses = await asyncio.gather(
        #     )
        # print(f'Status for {url}: {statuses}')
        for finished_task in asyncio.as_completed(requests):
            print(await finished_task)


asyncio.run(main())