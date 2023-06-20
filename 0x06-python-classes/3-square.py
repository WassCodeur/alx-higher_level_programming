#!/usr/bin/python3
"""area of a square"""


class Square:
    """class Square based on 2-square.py"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """
    public instance method: def area(self)
    return current square area
    """
    def area(self):
        return (self.__size ** 2)
