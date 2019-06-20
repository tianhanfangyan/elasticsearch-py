#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch


# connection
es = Elasticsearch(["connection"])

# bucket record
def bucket_record():
    body = {
        "query": {
            "match_all": {}
        },
        "aggs": {
            "name": {
                "terms": {
                    "field": "name",
                    "size": 10000
                },
                "aggs": {
                    "sum_age": {
                        "sum": {
                            "field": "age"
                        }
                    }
                }
            }
        }
    }

    res = es.search(index="test", body=body, request_time=60*3)
    print(res)