#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
if (number < 0):
    number = ((number * -1) % 10) * -1
else:
    number = number % 10

if (number > 5):
    print(f"{number} and is greater than 5")
elif (number == 0):
    print(f"{number} and is 0")
elif (number < 6):
    print(f"{number} and is less than 6 and not 0")
