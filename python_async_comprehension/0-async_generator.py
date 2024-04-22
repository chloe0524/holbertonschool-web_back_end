#!usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times"""
    for last_project_of_the_week in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
