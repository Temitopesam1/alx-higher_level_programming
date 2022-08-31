#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    s = ""
    o = 0
    for i, j in a_dictionary.items():
        if o < j:
            o = j
            s = i
    return s
