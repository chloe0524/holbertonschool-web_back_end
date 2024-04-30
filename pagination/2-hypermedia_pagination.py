#!/usr/bin/env python3
"""function named 'index_range'"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return tuple of size two containing start index + end index"""
    start_here = (page - 1) * page_size
    end_here = start_here + page_size
    return start_here, end_here


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes two integer args + return the right page of the 'dataset'"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()) or start < 0:
            return []
        return self.dataset()[start:end]

    import math

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with pagination information."""
        data = self.get_page(page, page_size)
        prev_page, next_page = None, None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        return {
            "page_size": page_size,"page": page,
            "data": data,
            "next_page": next_page, "prev_page": prev_page,
            "total_pages": total_pages
        }
