#!/usr/bin/env python3
"""function 'sum_mixed_list' = 'list mxd-lst' returns sum'"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return 'mxd_lst' 'list' 'sum' 'float'"""
    return sum(mxd_lst)
