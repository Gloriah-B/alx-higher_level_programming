#!/usr/bin/python3
"""
Module: json_file_writer

Module serializes objects into JSON format and save them to files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save to JSON File Function

    Writes the JSON representation of the provided object to a file.

    Args:
        my_obj: The object to be serialized and saved to a JSON file
        filename (str): The name of the file to save the JSON rep

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
