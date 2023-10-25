#!/usr/bin/python3
def roman_to_int(roman_string):

    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0

    for i, j in zip(roman_string, roman_string[1:]):
        if i not in values.keys():
            return 0
        elif values[i] >= values[j]:
            number += values[i]
        else:
            number -= values[i]
    number += values[roman_string[-1]]
    return number
