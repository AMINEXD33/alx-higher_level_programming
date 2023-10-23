#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (value == None):
            return False
        value += 1
        print("{:d}".format(value - 1))
        return True
    except TypeError:
        return False
