import asyncio
import functools
import time
from typing import Callable, Any


async def delay(delay_second: int) -> int:
    print(f'sleeping for {delay_second} seconds')
    await asyncio.sleep(delay_second)
    print(f'finishing for {delay_second} seconds')
    return delay_second


def async_timed() -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f"starting {func.__name__} with args {args} {kwargs}")
            start_time = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end_time = time.time()
                total_time = end_time - start_time
                print(f"finished {func.__name__} in {total_time:.4f} seconds")

        return wrapped

    return wrapper


