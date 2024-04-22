#!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time

    Args:
        n (int): number of tasks to be executed
        max_delay (int): maximum delay in seconds for each task

    Return:
        float: average time per task
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_over = time.time()
    total_time = timeover - startingblock
    return float(total_time / n)
