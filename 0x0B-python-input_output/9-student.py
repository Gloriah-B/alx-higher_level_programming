#!/usr/bin/python3
"""
Module that defines the Student class.

Module includes the defn of the Student class, which reps a student
with attributes such as first name, last name, and age.
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
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """
        Returns a string representation of the Student instance.

        Returns:
            str: A string representation of the Student instance.
        """
        return f"Student('{self.first_name}', '{self.last_name}', {self.age})"

# Example usage:
# Create a Student instance


student1 = Student("Tom", "Smith", 89)
print(student1.to_json())

# Create another Student instance
student2 = Student("I have a long name", "A very long name, not you?", -89)
print(student2.to_json())

# Create another Student instance
student3 = Student("", "", 0)
print(student3.to_json())
