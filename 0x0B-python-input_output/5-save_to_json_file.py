#!/usr/bin/python3
"""import json"""
import json
def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
      using a JSON representation
      args:
          my_obj: object
          filename: name of the file
        return: None
    """
    with open(filename, mode='w', encoding='utf8') as myfile:
        to_json = json.dumps(my_obj)
        myfile.write(to_json)
