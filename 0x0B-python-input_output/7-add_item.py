#!/usr/bin/python3
"""5-save_to_json_file.py module and 6-load_from_json_file.py module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import os.path
if __name__ == "__main__":
    filename = "add_item.json"
    if os.path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
