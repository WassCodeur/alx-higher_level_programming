#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    # for i in range(len(set_1)):
    for i in set_1:
        if (i in set_2) is False:
            new_set.add(i)
    for j in set_2:
        if (j in set_1) is False:
            new_set.add(j)
    return new_set
