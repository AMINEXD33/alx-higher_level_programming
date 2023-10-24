#!/usr/bin/python3
"""SQUARE"""


class Square():
    """ititiate the square size"""
    def __init__(self, size=0):
        """Initialize the size attr
        size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size

    @property
    def size(self):
        """get the value of the protected attr"""
        return self.__size

    @size.setter
    def size(self, value):
        """set a new value to the protected attr"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
            return
        if value < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = value
    
    def area(self):
        """
        Calculate the area of a square
        return: the square area
        """
        return (self.__size * self.__size)
