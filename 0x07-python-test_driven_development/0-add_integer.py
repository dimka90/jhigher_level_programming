#!/usr/bin/python3
""" a module that defines two integer """


def add_integer(a, b=98):
    """
    a function that add two integers a and b must be int or float
    args:
        a - the first parameter
        b - the second parameter and it is set to 98 by default
    raise type error if a and b is not int or float
    cast a and b into integer if they are float
    then return addition of a and b
    """
    if type(a) is not int and type(a) is not  float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not  float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
