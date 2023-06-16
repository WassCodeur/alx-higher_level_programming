#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    result = dict(filter(lambda x: x[1] is not value, a_dictionary.items()))
    return result
