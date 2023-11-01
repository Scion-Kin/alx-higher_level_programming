#!/usr/bin/python3
for i in range(122, 97, -2):
    j = i - 33
    print("{0}{1}".format(chr(i), chr(j)), end="")
