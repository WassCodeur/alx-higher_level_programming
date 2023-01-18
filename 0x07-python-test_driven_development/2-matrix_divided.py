#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    """
    args:
        matrix (list of lists): matrix to be divided
        div (int or float): divisor
    returns:
        new matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [
        [round(j / div, 2) for j in i]for i in matrix]
    return new_matrix