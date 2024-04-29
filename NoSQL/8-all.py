#!usr/bin/env python3
"""1"""

import pymongo

def list_all(mongo_collection):
    docs = mongo_collection.find()
    res = []
    for doc in docs:
        res.append(doc)
    return res
