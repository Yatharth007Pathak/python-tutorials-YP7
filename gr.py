"""
Stack Overflow
If we mistakenly write a recursive function without a proper base case, it will lead to a stack overflow.
"""

# Infinite Recursion Without a Base Case: The function infinite_recursion keeps calling itself indefinitely without a base case to terminate the recursion.

def infinite_recursion():
    return infinite_recursion()

infinite_recursion()  # This will eventually raise a RecursionError