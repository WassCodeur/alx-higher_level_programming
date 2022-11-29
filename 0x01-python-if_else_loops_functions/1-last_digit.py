#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = number % 10
if number < 0:
    Last_digit = number % -10
if Last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, Last_digit))
elif Last_digit == 0:
    print("Last digit of {} is {}".format(number, Last_digit))
elif Last_digit < 5:
    print("Last digit of {} is {} and is less than 5".format(number, Last_digit))    
