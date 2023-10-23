#!/usr/bin/python3
class CSEX(Exception):
    pass
def raise_exception_msg(message=""):
    raise CSEX(message)