#!/usr/bin/python3
"""Defines an addition of integers function."""


def add_integer(a, b=98):
    """Return the result of addition of a and b.

    Float arguments are typecasted to integers before calculating.

    Raises:
        TypeError: if a or b are neither integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
