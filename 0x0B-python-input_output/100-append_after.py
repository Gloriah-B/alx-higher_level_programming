#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text after each line with specific string in a file

    Args:
    - filename (str): Name of the file to modify.
    - search_string (str): String to search for in each line of the file.
    - new_string (str): String to append aftr each line with search_string

    Note:
    - Uses the with statement to manage file handling.
    """
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()

        file = open(filename, 'w')
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.close()
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
