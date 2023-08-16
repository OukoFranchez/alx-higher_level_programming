#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for row in matrix:
        row_squared = []
        for element in row:
            element_squared = element * element
            row_squared.append(element_squared)

        matrix_squared.append(row_squared)
    return matrix_squared
