#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    for i in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            idx += 1
        except IndexError:
            pass
    print("")
    return idx
