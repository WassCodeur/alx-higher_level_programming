#!/usr/bin/python3
"""size validation"""


class Square:
    """Class Square based on 1-square.py"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
