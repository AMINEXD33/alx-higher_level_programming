#!/usr/bin/python3
"""inherit from list, return the list in order
"""


class Mylist(list):
    def __init__(self):
        """inherit all attr and functions"""
        super().__init__()

    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
