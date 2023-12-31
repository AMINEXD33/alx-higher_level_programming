#!/usr/bin/python3
"""Geometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Geometry class"""
    def __init__(self, width, height):
        """construc"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return (self.__height * self.__width)

    def __str__(self):
        """when priting the instance"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
