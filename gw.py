# Infinite Recursive Function: An infinite recursive function is a function that keeps calling itself without ever reaching a base case.


def infinite_recursion():
    print("Calling infinite_recursion()")
    infinite_recursion()

infinite_recursion()

'''
Explanation: The function infinite_recursion() calls itself repeatedly without a base case, 
leading to infinite recursion. Python will eventually raise a RecursionError when the maximum recursion depth is exceeded.
'''