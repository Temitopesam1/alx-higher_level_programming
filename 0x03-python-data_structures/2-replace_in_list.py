#!/usr/bin/python3
<<<<<<< HEAD
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
=======
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
>>>>>>> 44c7d9cf9f2a463e697ff8d7e1e67459377c43e1
