#!/usr/bin/python3
"""This module contains a function that returns the JSON representation of an object (string)
"""
import json
def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string)
    args:
        my_obj: object
    return: JSON representation of an object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
