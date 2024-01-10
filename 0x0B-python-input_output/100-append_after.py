#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Append line of text after each line with specific string in a file

    Args:
    - filename (str): Name of the file to modify.
    - search_string (str): String to search for in each line of the file.
    - new_string (str): String to append aftr each line with search_string

    Note:
    - Uses the with statement to manage file handling.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    # Example usage:
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
