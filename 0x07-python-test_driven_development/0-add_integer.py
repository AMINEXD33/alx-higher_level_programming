#!/usr/bin/python3
"""
This module contains a function that adds two numbers


"""


def add_integer(a, b=98):
    """add two integers or floats Note: the floats will be casted to int
    Args: a: first int b: second int
    Returns: The num1+num2 Raises: TypeError: if a or b are not an int/float"""
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
        return
    elif (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
        return
    # cast to int
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a+b)
