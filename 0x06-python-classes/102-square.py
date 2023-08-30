#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    Represents a square and provides methods to calculate
    its area and compare it with other squares.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get/set the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compare the area of the square with another square for equality.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare the area of the square with another square for inequality.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare the area of the square with another square for less than.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is less than the other square's area,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare the area of the square with
        another square for less than or equal to.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is less than or equal
            to the other square's area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare the area of the square with another square for greater than.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is greater than
            the other square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare the area of the square with another
        square for greater than or equal to.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is greater than or
            equal to the other square's area, False otherwise.
        """
        return self.area() >= other.area()
