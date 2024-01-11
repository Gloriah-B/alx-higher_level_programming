#!/usr/bin/python3
"""
Module tht insert line of text aftr each line containing specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text to file after each line containing a specific string

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line
        new_string (str): The line of text to be inserted after each line
        containing the search string
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # File doesn't exist, no need to append
        return

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

# Example usage:
# append_after("example.txt", "specific", "Inserted Line\n")
