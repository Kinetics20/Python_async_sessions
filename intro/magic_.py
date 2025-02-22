import asyncio
from asyncio import Future
from typing import Callable

import aiohttp


class Fetch(Future):
    def __init__(self, url: str) -> None:
        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        super().__init__()
        task = loop.create_task(self._fetch(url))
        self.result = None

        loop.run_until_complete(task)



    async def _fetch(self, url: str) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                self.set_result(data)

    def then(self, callback: Callable) -> None:
        self.add_done_callback(lambda future: callback(self.result()))



def fetch_data(url: str) -> None:
    data = yield Fetch(url)
    print(data)



url_ = "https://api.nbp.pl/api/exchangerates/rates/a/eur"
gen_data = fetch_data(url_)
next(gen_data).them(lambda x: gen_data.send(x))

