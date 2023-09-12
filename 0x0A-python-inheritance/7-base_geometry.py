#!/usr/bin/python3
"""Module for task 7"""


class BaseGeometry:
    """
    A base class that provides a blueprint for other geometry classes.

    Methods:
    - area(): Placeholder method to be overridden by subclasses
                for calculating the area of a specific geometry.
    - integer_validator(name, value): Validates that a given value is
                an integer and greater than zero.
    """

    def area(self):
        """
        Placeholder method to be overridden by subclasses
        for calculating the area of a specific geometry.
        Raises:
            Exception: This method should be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """
        Validates that a given value is an integer and greater than zero.
        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
