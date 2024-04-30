#!/usr/bin/env python3
"""function named 'index_range'"""


def index_range(page: int, page_size: int) -> tuple:
    """return tuple of size two containing start index + end index"""
    start_here = (page - 1) * page_size
    end_here = start_here + page_size
    return start_here, end_here
