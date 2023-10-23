#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for div in range(1, 3):
        try:
            if div > a:
                raise Exception("Too far")
            else:
                result += (a**b)/div
        except:
            result = b + a
            break
    return result

#import dis
#dis.dis(magic_calculation)
