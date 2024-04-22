#!/usr/bin/env python3
"""'measure_runtime''coroutine'will 'execute' 'async_comprehension' 4 times """
import asyncio
import timeit

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """'measure' 'runtime'"""
    start_time = timeit.default_timer()
    await asyncio.gather(*(async_comprehension()
                         for _ in range(4)))
    end_time = timeit.default_timer()
    total_run = end_time - start_time
    return total_run
