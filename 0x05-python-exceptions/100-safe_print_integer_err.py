#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        value -= 1
        print("{:d}".format(value + 1))
    except TypeError:
        sys.stderr.write("{} is not an integer".format(value))
