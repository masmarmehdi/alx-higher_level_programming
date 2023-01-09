#!/usr/bin/python3
"""Defines a Square that inherits from a Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a new Square"""
    def __init__(self, size):
        """
        Initialization of a new square

        Args:
            size (int): The size of the current square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
