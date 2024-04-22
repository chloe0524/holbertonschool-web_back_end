#!/usr/bin/env python3
"""'task_wait_random' that takes int 'max_delay' and returns 'asyncio.Task'"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """asyncio task to execc wait_random with max_delay"""
    return asyncio.create_task(wait_random(max_delay))
