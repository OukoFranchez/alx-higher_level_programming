#!/usr/bin/python3

"""This module provides classes for handling certain task 4.

Classes:
    Square: Defines a square.
"""


class Square:
    """
    Represents a square shape and provides methods to calculate its area.

    Args:
        size (int): The size of the square. Defaults to 0.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is negative.

    Example Usage:
    ```python
    # Create a square object with size 5
    square = Square(5)

    # Calculate the area of the square
    area = square.area()

    print(area)  # Output: 25
    ```
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

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for the size field.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size field.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
