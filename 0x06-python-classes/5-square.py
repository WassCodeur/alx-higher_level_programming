#!/usr/bin/python3
"""printing a square"""


class Square:
    """class square based on 6-square.py"""
    def __init__(self, size=0):
        """
        Initialisation
        Args: size(int) square size

        Returns: None
        """
        self.__size = size

    @property
    def size(self):
        """GET/SET value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    public instance method: def area(self)
    return current area
    """
    def area(self):
        return (self.__size ** 2)

    """
    public instance method: def my_print(self):
    that print the square
    """
    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
