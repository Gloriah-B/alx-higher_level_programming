#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0

    try:
        while printed < x:
            try:
                if isinstance(my_list[printed], int):
                    print("{:d}".format(my_list[printed]), end="")
                    count += 1
                printed += 1
            except (ValueError, TypeError):
                printed += 1
    except IndexError:
        pass

    print()
    return (count)
