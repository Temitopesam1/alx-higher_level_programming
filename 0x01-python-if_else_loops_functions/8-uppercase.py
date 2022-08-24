#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        asci = ord(str[i])
        if asci in range(97, 123):
            asci -= 32
        print(f"{}".format(chr(asci)), end="")
        print()
