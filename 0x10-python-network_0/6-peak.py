#!/usr/bin/python3
""" Finds a peak inside a list """


"""def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    li = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return li[mid]
    elif mid - 1 < 0:
        return li[mid] if li[mid] > li[mid + 1] else li[mid + 1]
    elif mid + 1 >= length:
        return li[mid] if li[mid] > li[mid - 1] else li[mid - 1]

    if li[mid - 1] < li[mid] > li[mid + 1]:
        return li[mid]

    if li[mid + 1] > li[mid - 1]:
        return find_peak(li[mid:])
    return find_peak(li[:mid])
"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    mid = length // 2
    li = list_of_integers
    if mid == length - 1:
        if li[0] > li[1]:
            return li[0]
        else:
            return li[1]
    elif li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
        return li[mid]
    elif li[mid - 1] >= li[mid]:
        return find_peak(li[:mid])
    elif li[mid + 1] >= li[mid]:
        return find_peak(li[mid:])
    elif li[length - 1] > li[lenght - 2]:
        return li[lenght - 1]
