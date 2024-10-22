"""
Parameters vs. Arguments

Parameters:
Definition: Parameters are the variables listed inside the parentheses in the function definition. 
They act as placeholders for the values that will be passed to the function when it is called.
Purpose: Parameters define the inputs that a function expects.
Location: Parameters are found in the function definition.
Example:
def greet(name, age):                 # 'name' and 'age' are parameters
    print(f"Hello, {name}! You are {age} years old.")


Arguments:
Definition: Arguments are the actual values we pass to the function when you call it. 
These values are assigned to the corresponding parameters in the function.
Purpose: Arguments provide the data that the function will operate on.
Location: Arguments are found in the function call.
Example:
greet("Alice", 25)                    # "Alice" and 25 are arguments


Key Differences

Context:
Parameters are part of the function's definition, describing what inputs the function can accept.
Arguments are part of the function's invocation, providing the actual data to those parameters.

Role:
Parameters are like placeholders or variables that define what kind of data the function expects.
Arguments are the actual data values that are passed to the function when it is called.
"""


def multiply(a, b):  # 'a' and 'b' are parameters
    return a * b

result = multiply(2, 3)  # 2 and 3 are arguments
print(result)  # Output: 6