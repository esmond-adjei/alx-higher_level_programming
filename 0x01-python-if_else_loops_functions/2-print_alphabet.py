#!/usr/bin/python3
for c in range(97, 123):
    if c == 122:
        print("{0}".format(chr(c)))
    else:
        print("{0}".format(chr(c)), end='')
