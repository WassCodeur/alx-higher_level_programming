#!/usr/bin/python3
"""Module 8-rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Rectangle class
    """
    def __init__(self, width, height):
        """Instantiation of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """Area of rectangle
        """
        return self.__width * self.__height
    def __str__(self):
        """String representation of rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
