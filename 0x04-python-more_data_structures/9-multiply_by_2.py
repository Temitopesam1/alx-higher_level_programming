#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = a_dictionary.copy()
    for i, j in s.items():
        s.update({i: j * 2}) 
    return s
