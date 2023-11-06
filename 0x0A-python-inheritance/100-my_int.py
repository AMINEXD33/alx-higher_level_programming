#!/usr/bin/python3
"""miss around with the int class"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, other_value):
        """changing the behavior of =="""
        # check the type fist

        if (type(other_value) is not int):
            if (issubclass(type(other_value), int)):
                return not (self == other_value)
            else:
                raise TypeError("Error")
        else:
            raise TypeError("Error")
