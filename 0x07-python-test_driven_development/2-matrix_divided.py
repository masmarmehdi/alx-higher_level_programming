#!/usr/bin/python3
"""Defines matrix division function."""

def matrix_divided(matrix, div):
    """
    Dividing all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers and floats.
        div (int/float): The divisior.
    Raises:
        TypeError: if the matrix doesn't contain integer or float values.
        TypeError: if the matrix row doen't have the same size.
        TypeError: if the divisor isn't a float or integer number.
        ZeroDivisionError: if the divisor is 0
    Returns:
        a new matrix which has the result of division.
    """
    if not all(isinstance(element, (int, float)) for element in [num for row in matrix for num in row]) or not all(isinstance(row, list) for row in matrix) or not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matirx (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
