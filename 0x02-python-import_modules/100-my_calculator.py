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
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in func.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        func = func[op]
        print("{:d} {} {:d} = {:d}".format(a, op, b, func(a, b)))
        exit(0)
