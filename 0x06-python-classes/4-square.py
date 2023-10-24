#!/usr/bin/python3
"""
Module 4-square
"""


class Square:
    """
    class Square definition
    """

    def __init__(self, size=0):
        """
        Initializes square

        Args:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.size = size

    @property
    def size(self):
        """"
        Get the size of the square.

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns the current square area
        """
        return (self.__size)**2
