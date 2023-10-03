#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        char = str[x]
        if (str[x] >= "a" and str[x] <= "z"):
            char = chr(ord(str[x])-32)
            print("{}".format(char), end="")
    print("")
