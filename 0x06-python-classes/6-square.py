#!/usr/bin/python3
"""
Module 6-square
"""


class Square:
    """
    class Square definition
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Args:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

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
        set the size of the square.


        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """"
        Get

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set

        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates area of square

        Returns the current square area.
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
