#!/usr/bin/python3
"""
a python script that gets the value of a header variable [ X-Request-Id ]
from a response
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
        value = html.get('X-Request-Id')
        print(value)
