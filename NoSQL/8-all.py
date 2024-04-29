#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """function to return the list"""
    docs = mongo_collection.find()
    res = []
    for doc in docs:
        res.append(doc)
    return res
