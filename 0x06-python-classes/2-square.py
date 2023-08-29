#!/usr/bin/python3

"""This module provides classes for handling certain task 2.

Classes:
    Square: Defines a square.
"""


class Square:
    """
    Represents a square shape
    """

    def __init__(self, size=0):
        """
        Initializes a square object with the given size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
