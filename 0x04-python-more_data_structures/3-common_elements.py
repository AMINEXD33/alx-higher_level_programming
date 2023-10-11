#!/usr/bin/python3
def common_elements(set_1, set_2):
    dict_ = {}
    list_ = 0
    result = []
    if (len(set_1) <= len(set_2)):
        list_ = 1
    else:
        list_ = 2

    if list_ == 1:
        for x in set_1:
            if x in set_2:
                result.append(x)
    else:
        for x in set_2:
            if x in set_1:
                result.append(x)
    return (result) 
