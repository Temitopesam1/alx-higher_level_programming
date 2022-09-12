#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    a = 0
    while a is not x:
        try:
            print("{}".format(my_list[a]), end=" ")
            a += 1
        except:
            None
    print()
    return (a)
