#!/usr/bin/python3

if __name__ == "__main__":
    import sys

a = "argument"
b = "arguments"


if len(sys.argv) < 2:
    print("{} {}.".format(len(sys.argv) - 1, b))
elif len(sys.argv) == 2:
    print("{} {}:".format(len(sys.argv) - 1, a))
else:
    print("{} {}:".format(len(sys.argv) - 1, b))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
