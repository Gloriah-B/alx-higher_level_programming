#!/usr/bin/python3

"""Module defining the Student class."""


class Student:
    """Defines a Student by public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of strings representing attributes.
                If provided, only these attributes will be retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
                }

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with provided JSON.

        Args:
            json (dict): Dictionary representing attributes to replace.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
