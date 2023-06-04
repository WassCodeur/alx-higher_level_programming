#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    size = len(my_list)
    for i in range(size):
        if my_list[i] == 'c' or my_list[i] == 'C':
            my_list[i] = ''
    return ("".join(my_list))
