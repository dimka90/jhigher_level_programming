#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.keys())

    for key in sort_dict:
        value = a_dictionary[key]
        print(f"{key}: {a_dictionary[key]}")
