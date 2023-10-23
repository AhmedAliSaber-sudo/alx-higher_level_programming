#!/usr/bin/python3
for i in range(0, 26):
    print('{:c}'.format(i) if i % 2 == 0 else chr(i-32), end='')
