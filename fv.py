"""
In Python, parameters are the variables listed inside the parentheses in a function definition. 
These parameters act as placeholders for the values (arguments) that will be passed to the function when it is called. 
Parameters allow functions to accept input and work with data dynamically.

Types of Parameters in Python:

Positional Parameters:
Parameters that are assigned values based on the position of the arguments passed during the function call.

Keyword Parameters:
Parameters that are passed by explicitly naming them during the function call. This allows us to pass arguments out of order.

Default Parameters:
Parameters that have a default value specified in the function definition. 
If no argument is provided for that parameter during the function call, the default value is used.

Variable-Length Parameters:
*args: Allows a function to accept any number of positional arguments. These arguments are passed as a tuple.
**kwargs: Allows a function to accept any number of keyword arguments. These arguments are passed as a dictionary.

Order of Parameters
When defining a function, we should place the parameters in the following order:
Positional Parameters
Default Parameters
Variable-Length Positional Parameters (*args)
Keyword Parameters
Variable-Length Keyword Parameters (**kwargs)

example
def example_func(pos1, pos2, def1="default", *args, kw1, kw2, **kwargs):
    pass


In Python, arguments are the values that we pass to a function when we call it. These values are used by the function to perform its operations. 
Arguments correspond to the parameters defined in the function.

Types of Arguments:

Positional Arguments:
The most common type of argument. Arguments are passed to the function in the same order as the parameters are defined.

Keyword Arguments:
Arguments that are passed by explicitly naming the parameter they should be assigned to.
This allows us to pass arguments in any order.

Default Arguments:
Parameters that have a default value specified.
If no argument is provided for that parameter when calling the function, the default value is used.

Variable-Length Arguments:
Allows a function to accept an arbitrary number of arguments.
*args: Used to pass a variable number of positional arguments.
**kwargs: Used to pass a variable number of keyword arguments.
"""


# Positional parameters or arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 25)  # Output: Hello, Alice! You are 25 years old.


# Keyword parameters or arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet(age=25, name="Alice")  # Output: Hello, Alice! You are 25 years old.


# Default parameters or arguments
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice")  # Output: Hello, Alice! You are 30 years old.
greet("Bob", 40)  # Output: Hello, Bob! You are 40 years old.


# Example of *args: 
def add(*args):
    return sum(args)
print(add(1, 2, 3))  # Output: 6
print(add(4, 5))     # Output: 9


# Example of **kwargs:
def greet(**kwargs):
    if "name" in kwargs and "age" in kwargs:
        print(f"Hello, {kwargs['name']}! You are {kwargs['age']} years old.")
    else:
        print("Hello, Guest!")
greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.
greet()                      # Output: Hello, Guest!

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York