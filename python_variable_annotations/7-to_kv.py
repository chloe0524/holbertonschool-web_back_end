#!/usr/bin/env python3
"""to_kv takes a 'string k' + an 'int OR float v' return 'tuple'"""


def to_kv(k: str, v: int or float) -> tuple:
    """return 'str' 'int/float'"""
    return k, float(v**2)
