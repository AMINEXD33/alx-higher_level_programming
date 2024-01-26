#!/usr/bin/python3
"""
Create a script that accepts a URL as input, 
sends a request to the specified URL, 
and presents the decoded utf-8 body of the response. 
Ensure proper handling of urllib.error.HTTPError exceptions and, 
in case of an exception, 
print: "Error code:" followed by the corresponding HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
