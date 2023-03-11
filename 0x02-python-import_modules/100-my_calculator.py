#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul
    
    argc = len(argv)
    if argc - 1 < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        func = add if op == "+" else (sub if op ==  "-" else (mul if op == "*" else div))
    print("{:d} {} {:d} = {:d}".format(a, op, b, func(a,b)))
    exit(0)
