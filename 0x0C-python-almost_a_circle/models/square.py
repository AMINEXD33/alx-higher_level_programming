#!/usr/bin/python3
"""Square module that represents a Square
with a size
"""
from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size,
                         size,
                         x,
                         y,
                         id)

    @property
    def size(self):
        """Get/Set the size of the square"""
        return (self.height)

    @size.setter
    def size(self, val: int):
        if (type(val) is not int):
            raise TypeError("width must be an integer")
        if (val <= 0):
            raise ValueError("width must be > 0")
        self.height = val
        self.width = val

    def __str__(self):
        """return a str represantation of this instance"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """ update the object's attrs
            use args if it exists,
            else use kwargs
            args:
                args: a list of arguments
                kwargs: a dict of args
        """
        attr_ = ["id",
                 "size",
                 "x",
                 "y"]
        if (len(args) != 0):
            for x in range(len(args)):
                if (x > len(attr_)-1):
                    break
                setattr(self, attr_[x], args[x])
        else:
            for key, val in kwargs.items():
                if (key == attr_[1]):
                    self.height = val
                    self.width = val
                elif (key in attr_):
                    setattr(self, key, val)

    def to_dictionary(self):
        """return a dictionary that has
            all attrs
        """
        return ({
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        })
