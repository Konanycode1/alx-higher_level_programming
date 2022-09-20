#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("last digit of {:d} is ".format(number), end="")

last = number % 10

if last > 5:
    print("last digit of {:d} is {} and is greater than 5".format(number, last), end="")
elif last == 0:
    print("last digit of {:d} is {} and is 0".format(number, last), end="")
else:
    print("last digit of {:d} is {} and is less than 6 and not 0".format(number, last), end="")
# YOUR CODE HERE
