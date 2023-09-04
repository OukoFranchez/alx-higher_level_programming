#!/usr/bin/python3
"""This module provides class for task 4
classes:
    Rectangle - defines a Rectangle
    """


class Rectangle:
    """
    Represents a rectangular shape and provides
    methods to set and retrieve the width and height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object with
        optional width and height parameters.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string Representation of the rectangle
        Returns:
          str: A string rep the rectangle using # chars
          """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(['#' * self.width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string Representation of the rectangle
        that can be used to recreate a new instance

        Returns:
           str: A string rep of the rectangle
           """
        return f"Rectangle({self.__width}, {self.__height})"
