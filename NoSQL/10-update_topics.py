#!/usr/bin/env python3
"""function that changes topics of a school doc based on the name"""

from pymongo import UpdateMany


def update_topics(mongo_collection, name, topics):
    res = mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return res
