#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        value -= 1
        print("{:d}".format(value + 1))
        return True
    except TypeError:
        print("Exception:{}".format(sys.exc_info()[1]), file=sys.stderr)
        return False