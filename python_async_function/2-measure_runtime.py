#!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import random
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Create measure_time to time wait_n + return total_time/n"""
    #!/usr/bin/env python3
"""measure_time with n + max_delay andmeasures total exec time """

import asyncio
import random
import timeit


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Create measure_time to time wait_n + return total_time/n"""
    startingblock = timeit.default_timer()
    await wait_n(n, max_delay)
    timeover = timeit.default_timer()
    total_time = timeover - startingblock
    final_time = total_time / n
    return final_time
