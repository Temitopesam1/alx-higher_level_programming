#!/usr/bin/python3
from hidden_4 import *

list = dir()
for st in list:
    if (st[0] == "_"):
        continue
    print(st)
