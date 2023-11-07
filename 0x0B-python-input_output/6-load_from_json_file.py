#!/usr/bin/python3
"""using json"""
import json


def save_to_json_file(my_obj, filename):
    """file -> obj"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loaod(f)
