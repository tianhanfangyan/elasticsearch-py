#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch

# connection
es = Elasticsearch(["connection"])

# search record
def search_record():
    body = {
        "query": {
            "match_all": {}
        }
    }
    res = es.search(index="test", body=body)
    print(res)
