#!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import random
import timeit

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """returns 'total_time / n'"""
    startingblock = timeit.default_timer()
    await wait_n(n, max_delay)
    timeover = timeit.default_timer()
    total_time = timeover - startingblock
    return total_time / n
