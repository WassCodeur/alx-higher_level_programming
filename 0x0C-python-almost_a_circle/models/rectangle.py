#!/usr/bin/python3
"""The rectangle Module
"""


from models import Base

class Rectangle(Base):
    """My class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returning private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setting private attribute
        """
        self.__width = value

    @property
    def height(self):
        """Returning private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setting private attribute
        """
        self.__height = value

    @property
    def x(self):
        """Returning private attribute
        """
        return self._x
    @x.setter
    def x(self, value):
        """Setting private attribute
        """
        self._x = value

    @property
    def y(self):
        """Returning private attribute
        """
        return self._y
    @y.setter
    def y(self, value):
        """Setting private attribute
        """
        self._y = value
