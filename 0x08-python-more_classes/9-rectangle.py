#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a class instance"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter of a rectangle"""
        perimeter = 0
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = (2 * (self.__width + self.__height))
        return (perimeter)

    def __str__(self):
        """return str"""

        rectangle = ""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        for i in range(self.__height):
            for _ in range(self.__width):
                rectangle += str(self.print_symbol)
            if i < (self.__height - 1):
                rectangle += '\n'
        return (rectangle)

    def __repr__(self):
        """string representation of the rectangle"""
        rectangle = "Rectangle(" + str(self.__width) + ", "
        rectangle += str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """delete an object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method
        arg:
           rect_1(Rectangle)
           rect_2(Rectangle)
        return:

            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            bigger_rect = 0
            if (rect_1.area() >= rect_2.area()):
                return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to return a square"""
        return cls(size, size)
