"""
In Python, variables are used to store data that you can reference and manipulate throughout your code.
We create a variable by assigning it a value using the = operator.
"""


''' Variable Declaration:
we don't need to declare a variable before using it. Just assign it a value.
The type of the variable is determined by the value assigned. '''
age = 25        # Integer
age_ = "30"     # String
height = 5.9    # Float
name = "John"   # String
b = False       # Boolean
print(age, age_, height, name, b)
print(age, age_, height, name, b, sep = " & ")
print(age, age_, height, name, b, end = " * ")
print("my name is " + name + " and my age is " + age_)    # can only concatenate string to string
print("my name is " + name + " and my age is " + age_)
print("my name is " + name + " and my age is ", age)
print("my height is", height, "I am a student is", b)
print("my age has changed to", age + 1)

''' Dynamic Typing:
Python is dynamically typed, meaning the type of a variable is determined at runtime and can change as needed. '''
var = 10      # var is an integer
print(var)
var = "Text"  # Now var is a string
print(var)


''' Variable Names:
Must start with a letter (a-z, A-Z) or an underscore (_). Can contain letters, digits, and underscores. Cannot start with a number.
Use descriptive names and separate words with underscores (e.g., user_age), and use all uppercase letters for constants (e.g., MAX_SIZE).
Variable names are case-sensitive (age, Age, and AGE are different variables).
A variable name cannot be any of the python keywords. '''
user_name = "Alice"
max_retries = 5
print(user_name, max_retries)

''' Scope:
Local Scope: Variables defined inside a function are local to that function.
Global Scope: Variables defined outside any function are global and can be accessed anywhere in the script. '''
x = 10  # Global variable
def my_function():
    y = 5  # Local variable
    print(x)  # Can access global variable
    print(y)  # Can access local variable
my_function()


''' Reassigning Values:
We can change the value of a variable at any time '''
count = 10
print(count)
count = count + 5  # count is now 15
print(count)


''' Multiple Assignments:
We can assign the same value to multiple variables or multiple values to multiple variables. '''
a = b = c = 100  # All variables are assigned 100
print(a, b, c)
x, y, z = 1, 2, 3  # x=1, y=2, z=3
print(x, y, z)


''' Constants:
While Python does not enforce constant values, conventionally, variables that are meant to be constants are written in uppercase. '''
PI = 3.14159
print(PI)


"""
Snake case and lower camel case are two different conventions for naming variables, functions, or other identifiers in programming. 
Here's a brief explanation of each:

1. Snake Case
Format: Words are written in lowercase and separated by underscores (_).
Example: my_variable_name, this_is_a_function
Usage: Snake case is commonly used in Python for variable and function names.

2. Lower Camel Case (also known as camelCase)
Format: The first word is written in lowercase, and each subsequent word starts with an uppercase letter, with no spaces or underscores.
Example: myVariableName, thisIsAFunction
Usage: Lower camel case is often used in JavaScript for variable and function names.

Both conventions are used to make code more readable by clearly separating words in identifiers. 
The choice between snake case and camel case often depends on the coding standards of the language or the development team.
"""