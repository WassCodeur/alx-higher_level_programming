#!/usr/bin/python3
"""
    contains class Square which implements Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        class Square implements Rectangle.
        Methods:
            __init__()
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """
            Overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.size)
