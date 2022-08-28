#!/usr/bin/python3
<<<<<<< HEAD
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
=======
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
      my_list[idx] = element
      return my_list
>>>>>>> 613d831b55cdb191b726d6fa87bef8391e42d857
