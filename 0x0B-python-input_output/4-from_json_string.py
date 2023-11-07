#!/usr/bin/python3
"""using json"""
import json


def from_json_string(my_str):
    """return a dict object"""
    obj = json.loads(my_str)
    return (obj)
