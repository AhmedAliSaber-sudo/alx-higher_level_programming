#!/usr/bin/python3
for n in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(n) if n % 2 == 0 else chr(n-32), end='')