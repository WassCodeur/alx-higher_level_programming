#!/usr/bin/python3


def find_peak(list_of_integers):
    peak_integer = 0
    if len(list_of_integers) == 0:
        return None
    else:
        for integer in list_of_integers:
            if integer > peak_integer:
                peak_integer = integer
        return peak_integer
