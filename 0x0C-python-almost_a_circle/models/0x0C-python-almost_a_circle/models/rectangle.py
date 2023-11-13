#!/usr/bin/python3
"""Rectangle module"""
from base import Base


class Helper_functions():
    """Helper functions"""
    # validating functions
    def validate_int(var, index):
        """checks if the var is of type int
           then checks if it's > 0
           Args:
                var: the var that will be checked
        """
        var_list = ["width", "height", "x", "y"]
        if (type(var) is not int):
            raise TypeError(f"{var_list[index]} must be an integer")
        if (var < 0):
            raise ValueError(f"{var_list[index]} must be > 0")


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the Rectangle class"""
        super().__init__(id)
        # check the vars
        Helper_functions.validate_int(width, 0)
        Helper_functions.validate_int(height, 1)
        Helper_functions.validate_int(x, 2)
        Helper_functions.validate_int(y, 3)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # getters
    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    # setters
    @width.setter
    def width(self, width):
        Helper_functions.validate_int(width, 0)
        self.__width = width

    @height.setter
    def height(self, height):
        Helper_functions.validate_int(height, 1)
        self.__height = height

    @x.setter
    def x(self, x=0):
        Helper_functions.validate_int(x, 2)
        self.__x = x

    @y.setter
    def y(self, y=0):
        Helper_functions.validate_int(y, 3)
        self.__y = y

    def area(self):
        """return the area of a rectangle"""
        return (self.height * self.width)

    def display(self):
        """display the rectangle,by respect
           to x and y
        """
        print('\n' * self.y, end="")
        for height_ in range(self.height):
            print(' ' * self.x, end="")
            for width_ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update the object's attrs
            use args if it exists,
            else use kwargs
            args:
                args: a list of arguments
                kwargs: a dict of args
        """
        attr_ = ["id",
                 "width",
                 "height",
                 "x",
                 "y"]
        if (len(args) != 0):
            for x in range(len(args)):
                if (x > len(attr_)-1):
                    break
                setattr(self, attr_[x], args[x])
        else:
            for key, val in kwargs.items():
                if (key in attr_):
                    setattr(self, key, val)

