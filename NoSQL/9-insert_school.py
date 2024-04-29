#!/usr/bin/env python3
"""function that inserts a new document in a collection"""

from pymongo import InsertOne


def insert_school(mongo_collection, **kwargs):
    """new document in a collection based on 'kwargs'"""
    docs = {}
    for k, v in kwargs.items():
        docs[k] = v
    res = mongo_collection.insert_one(document)
    return result.inserted_id
