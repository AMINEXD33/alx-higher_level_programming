#!/usr/bin/python3
"""miss around with the int class"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
