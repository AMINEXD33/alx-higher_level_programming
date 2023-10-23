#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value += 1
        print("{:d}".format(value - 1))
        return True
    except TypeError:
        return False
