#! /usr/bin/env python
#! coding:utf-8


import datetime
from elasticsearch import Elasticsearch

# connection
es = Elasticsearch(["connection"])

# write record
def write_record():
    body = {
        "name": "tianhanfangyan",
        "age": 20,
        "timestamp": datetime.datetime.now()
    }

    es.indices.create(index="test", body=body)
