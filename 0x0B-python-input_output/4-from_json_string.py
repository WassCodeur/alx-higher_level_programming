#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """This function returns an object
    (Python data structure) represented by a JSON string
    args:
        my_str: JSON string
    return: object (Python data structure)
    """
    return json.loads(my_str)
