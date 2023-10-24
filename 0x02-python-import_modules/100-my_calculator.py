#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    op = argv[2]
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, operations[op](a, b)))
