#!/usr/bin/python3
"""can I"""


def add_attribute(obj, attr, value):
    """add a new attribute"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
