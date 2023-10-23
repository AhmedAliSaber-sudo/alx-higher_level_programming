#!/usr/bin/python3
for n in range(25, -1, -1):
    if n % 2 == 0:
        print("{}".format(chr(n+65)), end="")
    else:
        print("{}".format(chr(n + 97)), end="")
