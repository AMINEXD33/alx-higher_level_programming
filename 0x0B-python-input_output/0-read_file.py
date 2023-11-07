#!/usr/bin/python3
"""Read files and stuff"""


def read_file(filename=""):
    """Read a file UNC=utf-8"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
