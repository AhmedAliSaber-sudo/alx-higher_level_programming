#!/usr/bin/python3
"""
Module 102-square
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

    def area(self):
        """
        Calculates area of square
        Returns the area
        """
        return (self.__size)**2

    def __eq__(self, other):
        """
        Compares if equal and returns the result
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compares if not equal and returns the result
        """
        return self.size != other.size

    def __lt__(self, other):
        """
        Compares if lesser than and returns the result
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        return self.size >= other.size

    @property
    def size(self):
        """"
        Get

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value