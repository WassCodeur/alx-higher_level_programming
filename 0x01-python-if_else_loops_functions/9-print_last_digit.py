#!/usr/bin/python3
def print_last_digit(number):
  if number < 0:
    number = number * -1
  Last_digit = number%10
  print(Last_digit,end="")
  return Last_digit
