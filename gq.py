"""
The call stack is a fundamental concept in computer science, particularly in programming languages like Python. 
It plays a crucial role in managing function calls, including recursive calls.

What is the Call Stack?4
The call stack is a stack data structure that stores information about the active subroutines (functions) of a computer program. 
When a function is called, information about the call is pushed onto the call stack, 
including the function's parameters, return address, and local variables. 
When the function completes, its information is popped from the stack, and control is returned to the function that made the call.

How the Call Stack Works with Recursive Calls
When a function calls itself (recursion), each recursive call is treated as a new function call and is pushed onto the call stack. 
The call stack helps keep track of where each recursive call is in the sequence so that the program knows where to return after each call completes.

Important Points About the Call Stack
Memory Usage:
Each function call consumes memory for storing function-specific information (like local variables).
For deep recursion (e.g., very large n in the factorial example), this can lead to a stack overflow if the stack memory limit is exceeded.

Base Case Importance:
Without a base case, the recursive calls would never stop, leading to infinite recursion and eventually a stack overflow.

Return Addresses:
The call stack keeps track of the return address for each function call, 
ensuring that control returns to the correct point in the program after the function completes.
"""

# Understanding the Call Stack with Factorial

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120

'''
Call Stack for factorial(5)

Initial Call: factorial(5)
The call stack pushes factorial(5).
Since n is not 0 or 1, the function proceeds to call factorial(4).

Second Call: factorial(4)
The call stack pushes factorial(4) on top of factorial(5).
Since n is not 0 or 1, the function proceeds to call factorial(3).

Third Call: factorial(3)
The call stack pushes factorial(3) on top of factorial(4).
Since n is not 0 or 1, the function proceeds to call factorial(2).

Fourth Call: factorial(2)
The call stack pushes factorial(2) on top of factorial(3).
Since n is not 0 or 1, the function proceeds to call factorial(1).

Fifth Call: factorial(1)
The call stack pushes factorial(1) on top of factorial(2).
Now, n is 1, so the base case is reached, and 1 is returned.

Unwinding the Call Stack:
The return value 1 from factorial(1) is used in factorial(2), which returns 2 * 1 = 2.
The return value 2 from factorial(2) is used in factorial(3), which returns 3 * 2 = 6.
The return value 6 from factorial(3) is used in factorial(4), which returns 4 * 6 = 24.
The return value 24 from factorial(4) is used in factorial(5), which returns 5 * 24 = 120.
The final result, 120, is returned to the initial call.

Visualization of the Call Stack
At the deepest point, the call stack would look something like this:
factorial(5)
factorial(4)
factorial(3)
factorial(2)
factorial(1)
As each recursive call completes, the stack unwinds (pops) until the initial call completes.
'''