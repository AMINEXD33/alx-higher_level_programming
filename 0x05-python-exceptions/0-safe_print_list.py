#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_n = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            real_n += 1
        except IndexError:
            print()
            return (real_n)
    print()
    return (real_n)
