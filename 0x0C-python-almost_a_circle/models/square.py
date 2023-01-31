#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of square class
        Args:
            size (int): size of the square
            x (int): x of the square
            y (int): y of the square
            id (int): id of the square
            return: None
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """String representation of square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    @property
    def size(self):
        """size getter"""
        return self.width
    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        """Update square class
        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
            return: None
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """Dictionary representation of square class"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}