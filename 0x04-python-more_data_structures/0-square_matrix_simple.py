#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    return ([[(x**2) for x in row] for row in matrix])
