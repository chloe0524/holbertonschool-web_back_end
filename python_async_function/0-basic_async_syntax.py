#!/usr/bin/env python3
"""'wait_random'coroutine 'waits'for 'random''delay' up+returns 'delay time'"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns 'delay' time."""
    temp = random.random() * max_delay
    await asyncio.sleep(temp)
    return temp
