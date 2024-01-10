#!/usr/bin/python3

"""
Module defines a class called Rectangle, inheriting from BaseGeometry
"""


class BaseGeometry:
    """
    A class defining basic geometry operations.
    """

    def area(self):
        """
        Public instance methd raises xcepton indicatin area() isnt implementd
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.

        Args:
        - width: Integer representing the width of the rectangle
        - height: Integer representing the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
        - int: The area of the Rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
        - str: The formatted string describing the Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
        - str: The formatted string describing the Rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
