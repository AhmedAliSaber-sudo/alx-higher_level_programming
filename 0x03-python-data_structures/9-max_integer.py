#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for n in my_list:
            if n > max_int:
                max_int = n
        return max_int
    else:
        return None
