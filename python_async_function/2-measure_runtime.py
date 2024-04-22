#!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """returns 'total_time / n'"""
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time()-start_time
    return total_time / n
