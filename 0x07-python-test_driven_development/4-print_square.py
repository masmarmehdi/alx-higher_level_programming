#!/usr/bin/python3
"""Defines the print of a square function."""

def print_square(size):
    """
    Printing a square

    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if the size of the square isn't an integer
        ValueError: if the value of the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print(" ")
