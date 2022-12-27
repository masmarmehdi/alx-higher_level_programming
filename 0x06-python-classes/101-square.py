#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0,0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the current position of the square."""
        if not all(isinstance(i, int) for i in value) or not all(number >= 0 for number in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ Returning the elements to be printed in the print function """
        self.my_print()
        return ("")
