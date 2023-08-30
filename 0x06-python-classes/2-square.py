#!/usr/bin/python3


"""
a class Square that defines a square
-private instantiaton with optional size=0
-size must be an integer otherwise it should raise a typeerror
with an exception message
-if size is less than 0 it should raise valueerror with exception message
"""


class Square:
    """
    a class square that defines a square, it takes in one arg.
    and it raises a tyeerror and value error when neccessary
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
