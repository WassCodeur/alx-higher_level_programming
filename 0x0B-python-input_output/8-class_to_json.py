#!/usr/bin/python3
"""That function convert a class to json"""


def class_to_json(obj):
    """That function convert a class to json
    
        args: obj

        returs: json
  
    """
    to_dict = obj.__dict__
    return to_dict
