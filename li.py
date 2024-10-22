"""
Module aliasing: Renaming the module at the time of import, using as keyword.
Module aliasing in Python allows you to give a module a shorter or more convenient name when importing it.

syntax:
import <ModuleName> as <alias name>
"""

import math as m
import random as r

# Using the aliased 'math' module to calculate the square root of a number
number = 16
sqrt_number = m.sqrt(number)
print(f"The square root of {number} is {sqrt_number}")

# Using the aliased 'random' module to generate a random number between 1 and 10
random_number = r.randint(1, 50)
print(f"A random number between 1 and 50 is {random_number}")                        