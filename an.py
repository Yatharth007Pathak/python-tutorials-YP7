"""
In Python, None is a special constant representing the absence of a value or a null value. 
It is the only value of the NoneType data type. When a function does not return anything, it implicitly returns None.
"""

# The type of None is NoneType
print(type(None))  # Output: <class 'NoneType'>

'''
Usage: None is often used as a placeholder for optional or default parameters, or to indicate that a variable has no value.
Comparison: None can be compared with other values. It's commonly used in conditions to check if a variable is set.
'''
a = None
if a is None:
    print("a has no value")

# Default parameters
def my_function(param=None):
    if param is None:
        param = []
    print(param)

# Return value
def no_return():
    pass

result = no_return()
print(result)  # Output: None

# Initialization
x = None
if x is None:
    print("x is not assigned a value yet")


'''
None is not equivalent to False, 0, or an empty string/list/dictionary.
None is often used as a sentinel value in functions and algorithms to indicate a special condition, 
such as an uninitialized variable or the end of a loop.
'''