#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of a new square

        Args:
            size (int): size of the square
            x (int): the x coordinate of the square
            y (int): the y coordinate of the square
            id (int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of the Square"""
        return "[Square] ({}) {}/{} - {}\
        ".format(self.id, self.x, self.y, self.size)
