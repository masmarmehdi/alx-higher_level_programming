#!/usr/bin/python3

"""Defines a rectangle class"""


class Rectangle:
    """Rectangle class

    Attribute:
        number_of_instances (int): The number of rectangle instances
        print_symbol (any): the symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the current width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return a string representation of th rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Printing a message after each deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
