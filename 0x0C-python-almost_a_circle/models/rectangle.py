#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class which inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x coordinate of the rectangle
            y (int) the y coordinate of the rectangle
            id (int): inherited by super method. id of the new rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the current width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the current x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the current x coordinate of the rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the current y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the current y coordinate of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle with the character #."""
        for i in range(self.y):
            print()
        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for m in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
        ".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the values of the attributes using args and kwargs

        Args:
            *args (tuple): attribute values.
                - 1st argument is id
                - 2nd argument is width
                - 3rd argument is height
                - 4th argument is x
                - 5th argument is y
            **kwargs (dict): key/value pair of the attributes
        """
        if len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Rectangle instance to dictionary represntation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
