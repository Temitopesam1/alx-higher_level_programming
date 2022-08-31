#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s = []
    for i in my_list:
        if i == search:
           i = replace
        s.append(i)
    return s
