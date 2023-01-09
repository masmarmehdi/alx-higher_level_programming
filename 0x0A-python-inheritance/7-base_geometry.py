#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if a parameter is an int and greater than 0

        Args:
            name (str): the name of the type
            value (int): the value specified
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less or equal 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greated than 0".format(name))
