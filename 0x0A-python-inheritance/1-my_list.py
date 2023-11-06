#!/usr/bin/python3
"""inherit from list, return the list in order
"""


class MyList(list):
    """inherit all attr and functions"""
    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
