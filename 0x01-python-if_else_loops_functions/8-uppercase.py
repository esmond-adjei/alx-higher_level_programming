#!/usr/bin/python3
def uppercase(str):
    up = ''
    for c in str:
        if ord(c) <= 123 and ord(c) >= 97:
            up += chr(ord(c)-32)
        else:
            up += c
    print("{0}".format(up))
