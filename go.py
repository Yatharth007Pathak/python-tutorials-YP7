"""
Recursion in Python refers to the process in which a function calls itself directly or indirectly to solve a problem. 
A recursive function typically breaks a problem down into smaller, more manageable subproblems, 
until it reaches a base case, a condition under which the recursion stops.

Key Components of Recursion
Base Case: The condition that stops the recursion.
Without a base case, a recursive function would keep calling itself indefinitely, leading to a stack overflow error.
Recursive Case: The part of the function where it calls itself with modified arguments, moving toward the base case.

When to Use Recursion
Recursion is useful when a problem can naturally be divided into similar subproblems.
It's often used in problems involving trees, graphs, and other hierarchical structures (e.g., traversing a tree).
Recursion can simplify the implementation of algorithms that would otherwise be complex with iterative approaches.

Pros and Cons of Recursion
Pros:
Simplifies the code, especially for problems that have a recursive structure.
Easier to implement and understand for problems like factorial, Fibonacci, and tree traversal.

Cons:
Recursive functions can lead to excessive memory usage and stack overflow if not implemented carefully, especially for large inputs.
Recursive solutions can be less efficient than iterative solutions, as they might involve repeated calculations.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Testing the factorial function
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(0))  # Output: 1


'''
Example of Recursion: Factorial
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
Factorial can be defined recursively as:

factorial(n) = n * factorial(n-1)
Base case: factorial(0) = 1

Explanation:
Base Case: if n == 0 or n == 1: return 1
The recursion stops when n is 0 or 1 because the factorial of 0 and 1 is 1.
Recursive Case: return n * factorial(n - 1)
The function calls itself with n-1, reducing the problem size until it reaches the base case.
'''