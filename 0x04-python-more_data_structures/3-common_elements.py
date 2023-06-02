#!/usr/bin/python3
def common_elements(set_1, set_2):
    for c_1 in set_1:
        for c_2 in set_2:
            if c_1 == c_2:
                c = c_1
    return c
