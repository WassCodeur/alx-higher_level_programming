#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    else:
        Number = 0
        RomanNumber = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string)):
            valueTemp = RomanNumber[roman_string[i]]
            if i == (len(roman_string) - 1):
                Number += valueTemp
            else:
                if RomanNumber[roman_string[i + 1]] > valueTemp:
                    Number =  Number - valueTemp
                else:
                    Number =  Number + valueTemp
                

    return Number