#!/usr/bin/python3
"""to JSON"""
import json


def to_json_string(my_obj):
    """Dump the object"""
    json_ = json.dumps(my_obj)
    return (json_)
