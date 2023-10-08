#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) <= 0:
        return None

    max_ = float("-inf")
    for x in my_list:
        if x > max_:
            max_ = x
    return max_
