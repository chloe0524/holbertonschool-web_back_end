#!/usr/bin/env python3
"""Python function that returns all students score"""


def top_students(mongo_collection):
    """top_students returns all students sorted by average score"""
    best_students = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
    return best_students
