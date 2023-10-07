#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list == None):
        return
    if (len(my_list) == 0):
        return
    len_ = len(my_list) * -1
    x = -1
    while (x >= len_):
        print("{}".format(my_list[x]))
        x -= 1
