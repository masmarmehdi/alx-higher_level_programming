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
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """Get the current x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the current x coordinate of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """Get the current y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the current y coordinate of the rectangle"""
        self.__y = value
