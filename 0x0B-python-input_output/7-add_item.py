#!/usr/bin/python3
"""load, add, save"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    file_list = load_from_json_file("add_item.json")
    for i in sys.argv[1:]:
        file_list.append(i)
    save_to_json_file(file_list, "add_item.json")
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")
