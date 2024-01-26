#!/usr/bin/python3
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as res:
    html = res.info()
    print(html.get('X-Request-Id'))
