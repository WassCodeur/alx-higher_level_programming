#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
tmp = number
if number < 0:
    last_digit = (number * -1) % 10
else:
    last_digit = number % 10

if tmp < 0:
    last_digit *= -1

print("Last digit of {} is ".format(tmp), end="")
if last_digit > 5:
    print("{} and greater than 5".format(last_digit))

elif last_digit == 0:
    print("{} and is 0".format(last_digit))

elif last_digit < 6:
    print("{} and is less than 6 and is not 0".format(last_digit))
