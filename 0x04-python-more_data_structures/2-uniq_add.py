#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_int = set()
    total = 0

    for num in my_list:
        if num not in uniq_int:
            uniq_int.add(num)
            total += num
    return total
