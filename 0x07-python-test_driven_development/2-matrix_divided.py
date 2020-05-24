#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = matrix
    if type(matrix) is not int and type(matrix) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not  float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = matrix/div

    return new
