#!/usr/bin/python3
def islower(c):
    if ((c >= "a" and c  <= "z") and c != ''):
        return True
    elif (c == ''):
        raise Exception
    else: return False
