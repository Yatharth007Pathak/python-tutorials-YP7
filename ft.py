"""
Scope of Variables
Variables defined inside a function are local to that function and cannot be accessed outside of it.
Variables defined outside any function have a global scope.
"""

def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x)     # Error: NameError: name 'x' is not defined