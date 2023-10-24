#!/usr/bin/python3
"""Describe a square"""


class Square():
    """square"""
    def __init__(self, size=0):
        """initialize attribute"""
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
