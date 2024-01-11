#!/usr/bin/python3
"""
Module that defines the Student class.

Module includes the def of Student class, which represents a student
with attributes such as first name, last name, and age
"""


class Student:
    """
    Reps a student with attributes such as first name, last name, and age

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: A dictionary representation of the Student instance
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

# Example usage:
# Create a Student instance


student = Student("John", "Doe", 25)
# Retrieve the dictionary representation
student_dict = student.to_json()

# Print the result
print(student_dict)
