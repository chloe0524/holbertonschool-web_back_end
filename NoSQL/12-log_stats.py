#!/usr/bin/env python3
"""script that provides stats about 'Nginx logs' from 'MongoDB'"""


from pymongo import MongoClient


def main(nginx_collection):
    counter_logs = nginx_collection.count_documents({})
    print("{} logs".format(counter_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # method=GET + path=/status
    count = nginx_collection.count_documents({"method": "GET",
                                             "path": "/status"})
    print("{} status check".format(count))


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx
    main(nginx_collection)
