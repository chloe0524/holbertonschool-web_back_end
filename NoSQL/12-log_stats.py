#!/usr/bin/env python3
"""script that provides stats about 'Nginx logs' from 'MongoDB'"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)

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
