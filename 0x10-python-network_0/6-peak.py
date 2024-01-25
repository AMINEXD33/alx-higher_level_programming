#!/usr/bin/python3
"""find_peak
    @pram list_of_integersof_integers: a list of integers
"""
def find_peak(list_of_integers):

    list_of_integers
    # if there is no list of integers return None
    if list_of_integers == []:
        return None
    length = len(list_of_integers)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
