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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with a dictionary.

        Assumes json will always be a dictionary where each key is a public
        attribute name and each value is the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)


# Correct output - reload with json of Student("John", "Snow", 25)
student = Student("John", "Snow", 25)
json_data = student.to_json()
student.reload_from_json(json_data)
expected_output = {'first_name': 'John', 'last_name': 'Snow', 'age': 25}
print(student.to_json() == expected_output)


# Correct output - { 'firstname': "Kevin", 'lastname': "Mc Joe", 'age': 43 }
student = Student("John", "Snow", 25)
json_data = {'first_name': "Kevin", 'last_name': "Mc Joe", 'age': 43}
student.reload_from_json(json_data)
print(student.to_json() == json_data)
