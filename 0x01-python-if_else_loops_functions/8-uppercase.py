#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
    	if (str[x] >= "a" and str[x] <= "z"):
    		print("{}".format(chr(ord(str[x])-32)), end="")
    	else:
    		print("{}".format(str[x]),end="")