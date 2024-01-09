#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Append Write Function

    Appends text to file (UTF-8 encoded) and returns no of characs added

    If the file doesn’t exist, it will be created.

    Args:
    - filename (str): The name of the text file (default: "")
    - text (str): The text to be appended to the file (default: "")

    Returns:
    - int: Number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
