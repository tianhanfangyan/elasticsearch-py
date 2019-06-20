#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch

# create connection
es = Elasticsearch(["connection"])

# delete index
def delete_index(index):
    if es.indices.exists(index):
        info = es.indices.delete(index=index)
        if info['acknowledged']:
            print("delete index success.")
            return True
        else:
            print("delete index failed.")
            return False
    else:
        pass
        # TODO
        # ADD your logic.
