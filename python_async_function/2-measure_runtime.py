#!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total exec time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_over = time.time()
    total_time = time_over - start_time
    return float(total_time / n)
