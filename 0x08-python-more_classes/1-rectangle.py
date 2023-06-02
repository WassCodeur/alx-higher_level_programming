#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:
    """__init__ method"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """setters and getters width"""
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the current width of the square."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """setters and getters height"""
    @property
    def height(self):
        return (self.__height)

    @width.setter
    def height(self, value):
        """Set the current height of the square."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
