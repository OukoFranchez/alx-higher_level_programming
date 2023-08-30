#!/usr/bin/python3

"""This module provides classes for handling certain task 5.

Classes:
    Square: Defines a square.
"""


class Square:
    """
    Represents a square shape and provides methods to calculate its area.

    Args:
        size (int): The size of the square. Defaults to 0.
        position (tuple): The position of the square. Defaults to (0, 0).

    Raises:
        TypeError: If the size is not an integer
        or if the position is not a tuple of 2 positive integers.
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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object with the given size.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If the size is not an integer
            or if the position is not a tuple of 2 positive integers.
            ValueError: If the size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        Getter method for the size field.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter method for the position field.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Setter method for the position field.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.

        If the size is 0, prints an empty line.
        Otherwise, prints a square made of '#' characters.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
