#!/usr/bin/python3
"""
Module: file_writer

This module provides functionality to write a string to a text file (UTF8) and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Write File Function

    Writes the provided text to a file (UTF-8 encoded) and returns the number of characters written.

    Args:
    - filename (str): The name of the text file (default: "")
    - text (str): The text to be written to the file (default: "")

    Returns:
    - int: Number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
