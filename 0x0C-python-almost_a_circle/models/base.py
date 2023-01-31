#!/usr/bin/python3
"""This module contains the BaseModel class"""
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiation of base class
        Args:
            id (int): id of the object
            return: None
        """
        if id is not None:
            """if id is not None, assign the public instance attribute id"""
            self.id = id
        else:
            """if id is None, increment __nb_objects and assign the new value to"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
