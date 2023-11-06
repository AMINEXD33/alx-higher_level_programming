#!/usr/bin/python3
"""Geometry module
"""


class BaseGeometry():
    """Geometry class"""
    def __init__(self, width, height):
        """construc"""
        integer_validator('width', width)
        integer_validator('height', height)
        self.width = width
        self.height = height

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
