#!/usr/bin/python3
"""using json"""
import json


def save_to_json_file(my_obj, filename):
    """obj-> json -> write to file"""
    json_txt = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json_txt)
