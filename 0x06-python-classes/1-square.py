#!/usr/bin/python3

"""This module provides classes for handling certain task 1.

Classes:
    Square: Defines a square.
"""


class Square:
    """
    Represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
