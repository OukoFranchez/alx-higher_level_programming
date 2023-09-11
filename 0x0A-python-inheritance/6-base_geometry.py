#!/usr/bin/python3
"""Module for task 6"""


class BaseGeometry:
    """
    This is the base class for other geometry classes.

    Methods:
    - area(): Raises an exception indicating that it is not implemented.
    """
    def area(self):
        """
        Raises:
            Exception: Indicates that the method should
            be implemented in the derived classes.
        """
        raise Exception("area() is not implemented")
