#!/usr/bin/python3

"""
This module defines a class called BaseGeometry.
"""

class BaseGeometry:
    """
    A class defining basic geometry operations.
    """

    def area(self):
        """
        Public instance method raises xcepton indicate area() isnt implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method to validate an integer value.

        Args:
        - name: A string representing the name of the value
        - value: An integer value to be validated

        Raises:
        - TypeError: If the value is not an integer
        - ValueError: If the value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
