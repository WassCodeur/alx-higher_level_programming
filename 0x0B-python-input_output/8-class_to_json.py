#!/usr/bin/python3
"""import json"""
import json
def class_to_json(obj):
    """That function convert a class to json
        args: obj
        returs: json
    """
    to_dict = obj.__dict__
    to_json = json.dumps(to_dict)
    return to_dict
