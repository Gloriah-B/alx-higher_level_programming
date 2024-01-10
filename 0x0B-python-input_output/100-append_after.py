#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Append textline after each line containing specific string in a file

    Args:
    - filename (str): Name of the file to modify.
    - search_string (str): String to search for in each line of the file
    - new_string (str): String to append after each line of search_string

    Note:
    - Uses the with statement to manage file handling.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
