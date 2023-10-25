#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return([num if num != search else replace for num in my_list])
    return None
