#!/usr/bin/env python3
"""'wait_random'coroutine 'waits'for 'random''delay' up+returns 'delay time'"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns 'delay' times in ascending order."""
    lists_task = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        lists_task.append(task)
    delays = await asyncio.gather(*lists_task)
    for i in range(len(delays)):
        for j in range(len(delays) - 1):
            if delays[j] > delays[j + 1]:
                temp = delays[j]
                delays[j] = delays[j + 1]
                delays[j + 1] = temp
    return delays
