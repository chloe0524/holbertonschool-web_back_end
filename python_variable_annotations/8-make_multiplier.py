#!/usr/bin/env python3
"""make_multiplier that takes a 'float' multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """'multiply' 'floats'"""
    return lambda n: (n * multiplier)
