"""
Recursion is a technique where a function calls itself to solve smaller instances of the same problem.
The base case stops the recursion, and the recursive case moves toward the base case.
Recursion is particularly useful for problems that have a naturally recursive structure, 
but care must be taken to avoid inefficiencies and stack overflow.
"""


def fibonacci(n):

    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Recursive case: sum of the two preceding numbers
    else:        
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the Fibonacci function
n = int(input("Enter n: "))
print(fibonacci(n))  

for i in range(1, n+1):
    print(fibonacci(i), end = " ")


'''
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. It can be defined recursively as:

fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)
Base cases: fibonacci(0)=0, fibonacci(1)=1

Explanation:
Base Cases: if n == 1: return 0, elif n == 2: return 1
The recursion stops when n is 1 or 2 because these are the starting points of the Fibonacci sequence.
Recursive Case: return fibonacci(n - 1) + fibonacci(n - 2)
The function calls itself twice to calculate the previous two Fibonacci numbers.
'''