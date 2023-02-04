#!/usr/bin/python3
class Student:
    """class Student that defines a student by:
        Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name =first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
