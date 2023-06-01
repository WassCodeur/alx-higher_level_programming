#!/usr/bin/python3

class Square:
    """
        a class Square that defines a square by: (based on 1-square.py)
            Private instance attribute: size
            Instantiation with optional size: def __init__(self, size=0)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
