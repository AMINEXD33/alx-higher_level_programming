#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    if my_list is None or len(my_list) == 0:
        return None
    for x in my_list:
        if (x % 2) == 0:
            result.append(True)
        else:
            result.append(False)
    return result
