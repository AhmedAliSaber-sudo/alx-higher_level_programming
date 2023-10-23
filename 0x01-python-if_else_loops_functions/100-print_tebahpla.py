#!/usr/bin/python3
for i in range(0, 26):
    ch = ord('z') - i
    if i % 2 == 1:
        ch = (chr(c - ord('a') + ord('A')))
    else:
        ch = chr(ch)

    print("{}".format(ch), end="")
