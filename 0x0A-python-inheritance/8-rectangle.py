#!/usr/bin/python3
"""Module for task 8"""


class BaseGeometry:
    """
    A base class that provides a blueprint for other geometry classes.

    Methods:
    - area(): Raises an exception since it
    is not implemented in the base class.
    - integer_validator(name, value): Validates if the value is
    an integer and greater than 0.
    Raises a TypeError or ValueError if the validation fails.
    """

    def area(self):
        """
        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """
        Validates if the value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
