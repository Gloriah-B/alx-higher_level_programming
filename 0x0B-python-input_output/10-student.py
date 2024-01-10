#!/usr/bin/python3

"""Module defining the Student class."""


class Student:
    """Defines a student with attributes: first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
