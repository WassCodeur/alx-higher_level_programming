#!/usr/bin/python3

def remove_char_at(str, n):
    str_to_list = list(str)
    if len(str_to_list) > n and n >= 0:
        str_to_list[n] = ''
    new_str = "".join(str_to_list)
    return (new_str)
