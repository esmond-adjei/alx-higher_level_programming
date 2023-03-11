#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print("{:d} argument{}.".format(argc - 1, ""))

    else:
        print("{:d} argument{}:".format(argc - 1, "s" if argc > 2 else ""))
        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))
