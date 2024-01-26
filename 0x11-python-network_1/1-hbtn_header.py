#!/usr/bin/python3
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as res:
    header = res.info()
    print(header["X-Request-Id"])
