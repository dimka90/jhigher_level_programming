#!/usr/bin/python3
""" a class square that defines a square based on 4-square.py """


class Square:
    """
    a class that defines a square based on task 4.
    it will be able to call it self, and it takes in
    ""args: size.
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """
        a public instance that returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        you use a @property as getter to retrive size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        you use setter to a new parameter "value" to size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
         a public instance method that print
         in stdout the square with character #.
         if size is = 0 prints an empty line
        """
        if self.size == 0:
            print(" ")
        else:
            for _ in range(self.size):
                print("#" * self.size)
