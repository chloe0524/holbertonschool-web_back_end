#!usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""

import asyncio
import random


async def async_generator():
    """coroutine will loop 10 times"""
    for the_checker_will_be_the_death_of_me in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
