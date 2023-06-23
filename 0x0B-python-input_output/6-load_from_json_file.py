#!/usr/bin/python3
"""import json"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    args:
        filename: name of the file
    return: object
    """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        content = myfile.read()
        js_to_python = json.loads(content)
    return js_to_python
