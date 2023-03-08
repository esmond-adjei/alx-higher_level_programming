#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{0}".format(chr(c-32) if c % 2 == 1 else chr(c)), end='')
