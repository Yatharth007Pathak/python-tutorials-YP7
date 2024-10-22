"""
Steps to Create a Function:
Use the def Keyword: This keyword tells Python that we are defining a function.
Name our Function: Choose a descriptive name for our function. 
Function names should follow the same rules as variable names (e.g., start with a letter or underscore, no spaces).
Add Parameters (Optional): Inside the parentheses, we can list parameters that the function will accept. 
Parameters are optional; we can define a function with or without them.
Write the Function Body: This is the block of code that the function will execute. It is indented under the def statement.
Use a return Statement (Optional): If we want our function to return a value, use the return statement. 
This is optional, and if omitted, the function will return None by default.

Steps to Call a Function:
Calling a function in Python is the process of executing the function after it has been defined.
Use the Function Name: Type the name of the function we want to call.
Add Parentheses: Always include parentheses () after the function name, even if the function doesn't take any arguments.
Pass Arguments (If Needed): If the function requires arguments, pass them inside the parentheses.
"""

# Function to add two numbers
def add(a, b):
    result = a + b
    return result
# Function call
sum_value = add(5, 3)
print(sum_value)  # Output: 8


# Function to add two numbers
def addition(a, b):    # Function name: addition, Parameters: a, b
    result = a + b     # Function body: adds a and b, stores in result
    return result      # Function body: returns the result
print(addition(4,3))   # Output: 7


# Calling a Function Without Arguments
def greet():
    print("Hello, World!")
# Calling the function
greet()  # Output: Hello, World!


# Calling a Function with Arguments
def greet(name):
    print(f"Hello, {name}!")
# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!


# Calling a Function That Returns a Value
def add(a, b):
    return a + b
# Calling the function and storing the result
sum_value = add(5, 3)
print(sum_value)  # Output: 8


# Calling a Function Multiple Times
def multiply(x, y):
    return x * y

# Calling the function multiple times
product1 = multiply(2, 3)
product2 = multiply(5, 4)
print(product1)  # Output: 6
print(product2)  # Output: 20
