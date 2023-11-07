#!/usr/bin/python3
"""Read files and stuff"""


def write_file(filename="", text=""):
    """Read a file UNC=utf-8
       args:
           filename : the name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.writelines(text))
