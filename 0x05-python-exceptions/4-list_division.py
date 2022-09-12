#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lists = []
    ans = 0
    for a in range(list_length):
        try:
            ans = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            lists.append(ans)
    return (lists)
