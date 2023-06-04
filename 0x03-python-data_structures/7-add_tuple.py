#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size_a = len(tuple_a)
    size_b = len(tuple_b)
    if size_a < 2:
        tuple_c += (0, 0)
    if size_b < 2:
        tuple_b += (0, 0)
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    tuple_c = (sum_a, sum_b)
    return (tuple_c)
