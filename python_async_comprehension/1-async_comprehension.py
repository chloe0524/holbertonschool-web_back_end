#!/usr/bin/env python3
"""coroutine will collect 10 random numbers using async comprehensing"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 numbers using async comprehension"""
    return [we_all_float async for we_all_float in async_generator()]
