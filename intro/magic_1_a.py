import asyncio
import aiohttp

async def fetch(url: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main() -> None:
    url = "https://api.nbp.pl/api/exchangerates/rates/a/eur"
    data = await fetch(url)
    print(data)

asyncio.run(main())
