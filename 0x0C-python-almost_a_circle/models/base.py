#!/usr/bin/python3
"""
module for task 1
"""


class Base:
    """
    The `Base` class is a Python class that keeps
    track of the number of objects created from it.
    It assigns a unique ID to each object and increments
    the count of objects whenever a new object is created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new object of the `Base` class.
        If an ID is provided, it is assigned to the object.
        Otherwise, the count of objects is
        incremented and the new count is assigned as the ID.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
