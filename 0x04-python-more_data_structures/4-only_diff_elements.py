#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set_1 = set_1.difference(set_2)
    new_set_2 = set_2.difference(set_1)
    new_set = new_set_1.union(new_set_2)
    return (new_set)
