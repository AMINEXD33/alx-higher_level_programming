#!/usr/bin/python3
def fizzbuzz():
    for x in range(101):
        if (x % 2 == 0 and x % 3 == 0):
            print("Fizz Buzz", end=" ")
        elif (x % 3 == 0):
            print("Fizz", end=" ")
        elif (x % 2 == 0):
            print("Buzz", end=" ")
        else:
            print("{}".format(x), end=" ")
