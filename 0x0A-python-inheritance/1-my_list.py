#!/usr/bin/python3
"""Module 1-my_list.py"""
class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
