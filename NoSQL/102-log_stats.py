#!/usr/bin/env python3
"""script that provides stats about 'Nginx logs' from 'MongoDB'"""


from pymongo import MongoClient
from collections import Counter


def main(nginx_collection):
    """Prints stats about Nginx logs in MongoDB collection"""
    counter_logs = nginx_collection.count_documents({})
    print(f"{counter_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # method=GET + path=/status
    logs = nginx_collection.find({"method": "GET", "path": "/status"})
    print(f"{len(list(logs))} status check")

    ip_counter = Counter()
    for log in nginx_collection.find():
        ip_counter[log['ip']] += 1
    for ip, count in ip_counter.most_common(10):
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx
    main(nginx_collection)
