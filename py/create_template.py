#! /usr/bin/env python
#! coding:utf-8


from elasticsearch import Elasticsearch

# create connection
es = Elasticsearch(["connection"])

# create template
def create_template(name, index_patterns):
    body = {
        "order": 0,
        "version": 1,
        "index_patterns": [
            index_patterns
        ],
        "settings": {
            "index": {
                "number_of_shards": "32",
                "mapping": {
                    "ignore_malformed": "true"
                },
                "refresh_interval": "60s"
            }
        },
        "mappings": {
            "doc": {
                "_source": {
                    "enabled": True
                },
                "dynamic_templates": [
                    {
                        "string_fields": {
                            "match_mapping_type": "string",
                            "mapping": {
                                "type": "keyword"
                            }
                        }
                    }
                ],
                "properties": {
                    "time": {
                        "type": "date",
                        "format": "epoch_millis"
                    }
                }
            }
        }

    }

    es.indices.put_template(name=name, body=body)