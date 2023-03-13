#!/usr/local/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        tuple_a = (0, 0) if len_a == 0 else (tuple_a[0], 0)
    if len_b < 2:
        tuple_b = (0, 0) if len_b == 0 else (tuple_a[0], 0)

    s1 = tuple_a[0] + tuple_b[0]
    s2 = tuple_a[1] + tuple_b[1]
    return (s1, s2)
