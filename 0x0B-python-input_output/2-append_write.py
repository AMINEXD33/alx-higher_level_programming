#!/usr/bin/python3
"""files and stuff"""


def append_write(filename="", text=""):
    """APPEND T0  a file ENC=utf-8
       args:
           filename : the name of the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
