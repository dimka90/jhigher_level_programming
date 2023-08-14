#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    m = my_list[::-1]
    for a in m:
        print("{:d}".format(a))
