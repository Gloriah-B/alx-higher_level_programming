#!/usr/bin/python3
"""
Module for defining a Student class.
"""


class Student:
    """
    Dfns student by public instance attributes: first_name, last_name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes Student instance with given first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
