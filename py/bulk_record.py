#! /usr/bin/env python
#! coding:utf-8


import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


# connection
es = Elasticsearch(["connection"])

# bulk record
def bulk_record(index_name, index_type, data_list):
    actions = []
    i = 0

    for data in data_list:
        action = {
            "_index": index_name,
            "_type": index_type,
            "_id": str(i),
            "_source": {
                "name": data["name"],
                "age": data["age"],
                "timestamp": datetime.datetime.now(),
            }
        }
        i += 1
        actions.append(action)

    for success, info in bulk(client=es, actions=actions):
        if not success:
            print("a document failed.")
        else:
            pass

