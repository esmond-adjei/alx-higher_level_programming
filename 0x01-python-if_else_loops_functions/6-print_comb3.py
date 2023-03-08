#!/usr/bin/python3
for i in range(9):
    for j in range(1,10):
        if i != j and i < j:
            if i < 8 or j < 9:
                print("{0}{1}".format(i,j), end=', ')
            else:
                print("{0}{1}".format(i,j))
