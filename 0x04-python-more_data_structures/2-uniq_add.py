#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if i != j and my_list[i] == my_list[j]:
                my_list[i] = 0
        sum += my_list[i]
    return sum
