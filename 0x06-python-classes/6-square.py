#!/usr/bin/python3
""" a class that defines a square based on task 5-square.py """


class Square:
    """
    this will work just like task 5, but with additional
    args: position=(0, 0)).
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """
        a public instance that returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        using @property as the getter to retrive size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        using setter to set new parameter "value" to size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        using @property to retrive position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        a private instance attribute.
        position must be tupple of 2 positive integer
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        a public instance that prints in stdout the square with character #
        position should be use by using spaces when position[1] > 0
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            print("")
