#!/usr/bin/env python3
"""Task: A coroutine called async_generator that takes no
                 arguments.
                 The coroutine will loop 10 times, each time asynchronously
                 wait 1 second, then yield a random number between 0 and 10.Use the random module.
"""

import asyncio
import random
from typing import Generator 

async def async_generator() -> Generator[float, None, None]:
    """Generator that yields a random value between 0 and 10 every second,
        10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

# Example of how to use the async_generator
async def main():
    async for value in async_generator():
        print(value)
