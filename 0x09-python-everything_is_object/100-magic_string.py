#!/usr/bin/python3
def magic_string():
    magic_string.X = getattr(magic_string, "X", 0) + 1
    return ("BestSchool, "*(magic_string.X-1) + "BestSchool")
