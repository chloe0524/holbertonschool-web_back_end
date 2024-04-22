#!/usr/bin/env python3
"""to_kv takes a 'string k' + an 'int OR float v' return 'tuple'"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return 'str' 'int/float'"""
    return k, float(v**2)
