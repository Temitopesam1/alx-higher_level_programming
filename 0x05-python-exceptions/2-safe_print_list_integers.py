#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    length = 0

    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            length += 1
        except Except(ValueError, TypeError):
            None

    print()
    return (length)
