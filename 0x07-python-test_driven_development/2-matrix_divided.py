#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for index in row:
            if not isinstance(index, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        new_value = [round(x / div, 2) for x in row]
        new_matrix.append(new_value)
    return new_matrix
