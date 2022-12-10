#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        Last_digit = (number * - 1) % 10
    else:
        Last_digit = number % 10
    print("{:d}".format(Last_digit), end="")
    return Last_digit
