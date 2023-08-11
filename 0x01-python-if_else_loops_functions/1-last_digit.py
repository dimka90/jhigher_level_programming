#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastd = abs(number) % 10
print_output = "Last digit of " + str(number) + " is " + str(Lastd) + " and is"

if Lastd > 5:
    print(print_output, "greater than 5")
elif Lastd == 0:
    print(print_output, "0")
elif 0 < Lastd < 6:
    print(print_output, "less than 6 and not 0")
