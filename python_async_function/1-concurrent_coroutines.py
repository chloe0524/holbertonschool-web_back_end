#!/usr/bin/env python3
"""'wait_random'coroutine 'waits'for 'random''delay' up+returns 'delay time'"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns 'delay' times in ascending order."""
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    time_length = await asyncio.gather(*delays)
    for i in range(len(time_length)):
        for j in range(len(time_length) - 1):
            if time_length[j] > time_length[j + 1]:
                temp = time_length[j]
                time_length[j] = time_length[j + 1]
                time_length[j + 1] = temp
    return time_length
