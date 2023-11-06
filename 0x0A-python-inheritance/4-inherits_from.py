#!/usr/bin/python3
"""Return True if it's subclass"""


def inherits_from(obj, a_class):
    """Return"""
    
    if (type(obj) is a_class):
        return issubclass(type(obj), a_class)
    return False
