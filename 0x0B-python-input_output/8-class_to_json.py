#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """get the dict from the obj"""
    dict_ = {}
    if hasattr(obj, "__dict__"):
        dict_ = obj.__dict__.copy()
    return (dict_)
