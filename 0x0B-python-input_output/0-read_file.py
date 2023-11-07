#!/usr/bin/python3

"""Read a file UNC=utf-8"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
