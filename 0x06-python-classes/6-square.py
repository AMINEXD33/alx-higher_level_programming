#!/usr/bin/python3
"""SQUARE"""


class Square():
    """ititiate the square size"""
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """set a new value to the protected attr"""
        if type(position[0]) is not int or type(position[1] is not int):
            raise TypeError("size must be an integer")
            return
        if position[0] < 0 or position[1]:
            raise ValueError("size must be >= 0")
            return
        self.__position = position

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

    def my_print(self):
        """
        Print the square as '#'
        if the size is 0 , this function
        will print nothing
        """
        if (self.__position[1] != 0):
            print("\n"*self.__position[1], end="")
        if self.__size == 0:
            print()
            return
        else:
            for x in range(self.__size):
                if (self.__position[0] != 0):
                    print(" "*self.__position[0], end="")
                for y in range(self.__size):
                    print("#", end="")
                print("\n", end="")
