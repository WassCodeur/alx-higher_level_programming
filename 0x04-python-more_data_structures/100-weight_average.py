#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    total = 0
    result = 0
    if len(my_list) == 0:
        return 0
    for tple in my_list:
        if len(tple) == 0:
            tple[0] = 0
            tple[1] = 0
        elif len(tple) == 1:
            tple[1] = 0
        div += tple[1]
        total += (tple[0] * tple[1])
    return (total/div)
