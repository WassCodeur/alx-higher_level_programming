#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, mode="w", encoding='utf-8') as myfile:
        return myfile.write(text)
