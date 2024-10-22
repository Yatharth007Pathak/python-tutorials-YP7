"""
In Python, when we create a set with a mixture of different types of values, including boolean values (True and False), 
it might seem like the boolean values are not printed. 
This is because True and False in Python are actually treated as integers, with True equal to 1 and False equal to 0.
If our set contains integers 0 or 1, they will be treated the same as False and True, respectively, 
and since sets do not allow duplicate values, one of the equivalent values may not be shown
"""

mixed = {1, "apple", 3.14, True}
print(mixed) # Output: {'apple', 1, 3.14}

my_set = {True, 1, False, 0, 2, 3}
print(my_set) # Output: {False, True, 2, 3}

# True is equivalent to 1, so only one of them will appear in the set.
# False is equivalent to 0, so only one of them will appear in the set.