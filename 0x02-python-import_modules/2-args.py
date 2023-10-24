#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size))
    for index in range(size):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
