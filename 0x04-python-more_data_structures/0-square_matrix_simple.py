#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_line = []
        for j in range(len(matrix[i])):
            new_line.append((matrix[i][j])**2)
        new_matrix.append(new_line)
    return (new_matrix)
