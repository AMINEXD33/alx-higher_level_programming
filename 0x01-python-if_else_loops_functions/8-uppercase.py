#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
    	if (str[x] >= "a" and str[x] <= "z"):
    		print(chr(ord(str[x])-32), end="")
    	else:
    		print(str[x],end="")