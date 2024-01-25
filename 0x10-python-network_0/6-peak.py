#!/usr/bin/python3
"""find_peak
    @pram list_of_integers: a list of integers
"""


def find_peak(list_of_integers):

    ls = list_of_integers
    ls
    # if there is no list of integers return None
    if ls == []:
        return None
    length = len(ls)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if ls[mid] > ls[mid - 1] and ls[mid] > ls[mid + 1]:
            return ls[mid]
        if ls[mid - 1] > ls[mid + 1]:
            end = mid
        else:
            start = mid + 1
