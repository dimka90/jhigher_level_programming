#!/usr/bin/python3
def print_list_integer(my_list=[]):
    f_string = "{}\n" * len(my_list)
    fm_string = f_string.format(*my_list)
    print(fm_string, end="")
