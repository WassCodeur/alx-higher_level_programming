#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dist_sort = sorted(a_dictionary)
    for i in dist_sort:
        print("{}: {}".format(i, a_dictionary[i]))
