#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l_copy = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        l_copy[idx] = element
    return l_copy
