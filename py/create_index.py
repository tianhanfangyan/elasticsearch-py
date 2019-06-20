#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch

# create connection
es = Elasticsearch(["connection"])

# create index
def create_index(index):
    if es.indices.exists(index=index):
        return True
    else:
        info = es.indices.create(index=index)
        if info['acknowledged'] and info['shards_acknowledged'] and info['index'] == index:
            print("create index success.")
            return True
        else:
            print("create index failed.")
            return False
