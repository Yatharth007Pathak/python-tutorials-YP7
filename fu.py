"""
The return type of a function refers to the data type of the value that the function returns to the caller when it finishes executing. 
In Python, the return type is determined by the value that is returned by the return statement in the function.

Key Points About Return Types in Python:
Dynamic Typing: Python is dynamically typed, meaning that we don't need to explicitly declare the return type of a function. 
The return type is inferred based on the value that the function returns.
return Statement: The return statement is used to exit a function and pass back a value to the caller. 
The type of this value is the return type of the function.
Multiple Return Types: A function in Python can return different types of values, or even multiple values at once. 
The return type is flexible and can be of any Python data type, such as int, float, str, list, tuple, dict, etc.
No Return Value (None): If a function doesn't include a return statement, or if it has a return statement without a value, 
the function returns None, which is of the NoneType.
"""


# Returning a Single Value
def add(a, b):
    return a + b  # Returns an integer or float depending on inputs
result = add(5, 3)
print(result)  # Output: 8                                   Return Type: In this example, the return type is int when both inputs are integers.


# Returning a String
def greet(name):
    return f"Hello, {name}!"  # Returns a string
message = greet("Alice")
print(message)  # Output: Hello, Alice!                      Return Type: The return type here is str.


# Returning Multiple Values (Tuple)
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns a tuple of two integers
q, r = divide_and_remainder(10, 3)
print(q)  # Output: 3
print(r)  # Output: 1                                        Return Type: The return type in this case is a tuple containing two integers.



# Returning a List
def squares(numbers):
    return [x ** 2 for x in numbers]  # Returns a list of integers
result = squares([1, 2, 3, 4])
print(result)  # Output: [1, 4, 9, 16]                       Return Type: The return type here is list.


# No Explicit Return (NoneType)
def do_nothing():
    pass  # No return statement
result = do_nothing()
print(result)  # Output: None                                Return Type: The return type is NoneType because there is no return statement.