#!/usr/bin/python3
"""
module for task 2
"""


from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle shape
    with width, height, x-coordinate, and y-coordinate properties.
    Inherits from the `Base` class.
    Provides data validation for the properties.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a `Rectangle` object with
        the given width, height, x-coordinate, y-coordinate, and id.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of
            the rectangle.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.
            Defaults to 0.
            id (int, optional): The id of the rectangle.
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width property.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.
        Validates that the value is an integer and greater than 0.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("idth must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height property.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.
        Validates that the value is an integer and greater than 0.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate property.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate property.
        Validates that the value is an integer and greater than 0.

        Args:
            value (int): The x-coordinate value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate property.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate property.
        Validates that the value is an integer and greater than 0.

        Args:
            value (int): The y-coordinate value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
