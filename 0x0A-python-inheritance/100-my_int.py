#!/usr/bin/python3

"""
This module defines a class called MyInt, inheriting from int.
"""


class MyInt(int):
    """
    A class representing a rebel integer, inheriting from int.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.

        Args:
        - other: The other value to compare

        Returns:
        - bool: True if not equal; False if equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.

        Args:
        - other: The other value to compare

        Returns:
        - bool: True if equal; False if not equal
        """
        return super().__eq__(other)
