#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_n = 0
    try:
        for y in range(x):
            real_n += 1
            print(my_list[y], end="")
    except (OSError):
        return (real_n)
    return (real_n)
