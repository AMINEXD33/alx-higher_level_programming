#!/usr/bin/python3
def remove_char_at(str, n):
	cpy = ""
	print(cpy)
	for x in range(len(str)):
		if (x != n):
			cpy += str[x]
			
	return(cpy)