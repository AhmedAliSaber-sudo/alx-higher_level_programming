#!/usr/bin/python3
result = ""
for number in range(0, 100):

    if number < 10:
        result += "0{:d}, ".format(number)
    else:
        result += "{:d}, ".format(number)
    if number == 99:
        result = result.rstrip(', ')
print(result)
