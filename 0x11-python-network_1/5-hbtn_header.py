#!/usr/bin/python3
"""
get the value of a variable [X-Request-Id] 
found in the head of a response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)
