#!/usr/bin/python3
"""using json"""
import json


def load_from_json_file(filename):
    """file -> obj"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
