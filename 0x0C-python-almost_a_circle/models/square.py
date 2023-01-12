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

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and height of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square based on either args or kwargs

        Args:
            *args (tuple): attribute values.
                - 1st argument is id
                - 2nd argument is size
                - 3rd argument is x
                - 4th argument is y
            *kwargs (dict): key/value pair of the attributes
        """
        if len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init(self.id, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.id, self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns string representation of the Square"""
        return "[Square] ({}) {}/{} - {}\
        ".format(self.id, self.x, self.y, self.size)
