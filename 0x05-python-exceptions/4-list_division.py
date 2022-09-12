#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    ans = []
    for a in range(list_length):
        try:
            ans.append(my_list_1[a] / my_list_2[a])
        except TypeError:
            ans.append(0)
            print("wrong type")
        except IndexError:
            ans.append(0)
            print("out of range")
        except ZeroDivisionError:
            ans.append(0)
            print("division by 0")
        finally:
            pass
    return (ans)
