#!/usr/bin/python3
def uniq_add(my_list=[]):
    dict_ = {}
    sum_ = 0
    for x in my_list:
        try:
            if dict_[x] == True:
                pass
        except:
            sum_ += x
            dict_[x] = True
    return (sum_)
