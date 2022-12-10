#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_line = []
    for i in range(len(matrix)):
        new_line = []
        for j in range(len(matrix[i])):
            A = (matrix[i][j])**2
            new_line.append(A)
        new_matrix.append(new_line)
    return (new_matrix)
