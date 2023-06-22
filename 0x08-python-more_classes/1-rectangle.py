#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize a class instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """private instance attribute to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """instance attribute to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private attribute to set height"""
        return self.__height

    @height.setter
    def height(self, value):
        """instance attribute to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
