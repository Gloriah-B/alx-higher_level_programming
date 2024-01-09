#!/usr/bin/python3
"""
Module: file_writer

Module writes string to text file (UTF8) and returns no of characs written
"""


def write_file(filename="", text=""):
    """
    Write File Function

    Writes text to file (UTF-8 encoded) and returns no of xters written

    Args:
    - filename (str): The name of the text file (default: "")
    - text (str): The text to be written to the file (default: "")

    Returns:
    - int: Number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
