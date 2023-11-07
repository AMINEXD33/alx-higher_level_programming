#!/usr/bin/python3
"""using json"""
import json


def save_to_json_file(my_obj, filename):
    """obj-> json -> write to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
