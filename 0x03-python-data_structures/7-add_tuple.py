#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def print_tuple(tp=()):
        print("({}, {})".format(tp[0], tp[1]))
    lena, lenb = len(tuple_a), len(tuple_b)
    a1, a2, b1, b2 = 0, 0, 0, 0
    if lena < 2:
        if lena == 1:
            a1 = tuple_a[0]
    elif lena >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if lenb < 2:
        if lenb == 1:
            b1 = tuple_b[0]
    elif lenb >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)
    return new_tuple
