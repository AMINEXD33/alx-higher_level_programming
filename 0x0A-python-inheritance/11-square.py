#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.integer_validator(self, 'size', size)
        self.__size = size

    def area(self):
        """return the area"""
        return (self.__size**2)

    def __str__(self):
        """when instance is printed"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
