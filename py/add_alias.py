#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch

# create connection
es = Elasticsearch(["connection"])

# add alias
def add_alias(index, alias):
    if es.indices.exists_alias(index=index, name=alias):
        return True
    else:
        info = es.indices.put_alias(index=index, name=alias)
        if info['acknowledged']:
            print("add alias to index success.")
            return True
        else:
            print("add alias to index failed")
            return False
