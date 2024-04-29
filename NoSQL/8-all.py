#!usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """function to return the list"""
    res = list(mongo_collection.find())
    return res
