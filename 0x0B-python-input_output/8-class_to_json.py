#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
  """module class_to_json
 
       returns builds a dictionary

    """

    to_dict = obj.__dict__
    return to_dict
