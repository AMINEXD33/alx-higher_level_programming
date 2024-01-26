#!/usr/bin/python3
"""
 a script that accepts a URL as input,
 sends a request to the provided URL,
 and exhibits the decoded utf-8 body of the response.
 In cases where the HTTP status code is equal to or exceeds 400,
 print: "Error code:" followed by the HTTP status code value
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(body)
