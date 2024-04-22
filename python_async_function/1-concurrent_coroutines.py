#!/usr/bin/env python3
"""'wait_random'coroutine 'waits'for 'random''delay' up+returns 'delay time'"""

import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """returns 'delay' time."""
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return await asyncio.gather(*delays)
