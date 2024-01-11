#!/usr/bin/python3
"""
Module that insert a line of text after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line with specific string


    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): Line text inserted aftr each line wit search string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

# Example usage:
# append_after("example.txt", "specific", "Inserted Line\n")
