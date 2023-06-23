#!/usr/bin/python3
"""Module 10-square.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class
    """

    def __init__(self, size):
        """Instantiation of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of square
        """
        return self.__size ** 2

    def __str__(self):
        """String representation of square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
