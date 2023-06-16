#!/usr/bin/python3
def roman_to_int(roman_string):
    r_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    prev_value = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        roman_list = list(roman_string)
        for i in reversed(roman_list):
            current_value = r_num[i]
            if prev_value > current_value:
                number -= int(current_value)
            else:
                number += int(current_value)
            prev_value = current_value

        return number
