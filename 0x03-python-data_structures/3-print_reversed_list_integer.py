#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    while list_len > 0:
        list_len -= 1
        print("{:d}".format(my_list[list_len]))
