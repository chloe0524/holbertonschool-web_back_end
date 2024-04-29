#!/usr/bin/env python3
"""function that changes topics of a school doc based on the name"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school"""
    res = mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return res.modified_count
