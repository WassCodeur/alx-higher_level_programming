#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        size = len(line)
        for i in range(size):
            if i == (size - 1):
                print("{:d}".format(line[i]))
            else:
                print("{}".format(line[i]), end=" ")
