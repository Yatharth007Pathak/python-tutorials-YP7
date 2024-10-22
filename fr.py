"""
In Python, a function is a block of reusable code that performs a specific task. 
Functions allow us to organize our code into modular, manageable pieces, and they make it easier to reuse code across different parts of a program.

Key Concepts of Functions
Function Definition: We define a function using the def keyword, followed by the function name, parentheses (), and a colon :.
Inside the function, we write the code that we want to execute when the function is called.
Function Call: After defining a function, we can call (or invoke) it by using its name followed by parentheses. 
If the function requires arguments, we provide them inside the parentheses.
Parameters and Arguments:
Parameters: Variables listed inside the parentheses in the function definition.
Arguments: Values we pass to the function when we call it.
Return Statement: Functions can return a value using the return statement. 
If a function doesn't have a return statement, it returns None by default.
Scope: Variables defined inside a function are local to that function and cannot be accessed outside it.
Local variables are only accessible within the function they are defined in whereas global variables are accessible throughout the program.

Types of Functions
Built-in Functions: Python comes with many built-in functions like print(), len(), max(), min(), etc., which we can use without defining them.
User-defined Functions: These are functions that we define ourself using the def keyword.
Lambda Functions: Also known as anonymous functions, these are small functions defined using the lambda keyword 
and are generally used for short-term, simple operations.
"""

# Function definition
def greet(name):             # Function name is greet
    print("Hello", name, "!")
# Function call
greet("Alice")  # Output: Hello Alice !
greet("Bob")    # Output: Hello Bob !


# Function definition  
def greetings():             # Function name is greetings
    print("Hello World!")
# function call
greetings()     # Output: Hello world!


# Function definition
def hi():                    # Function name is hi
    print("hi everyone")
# Function call
hi()            # Output: hi everyone


# Lambda function to add two numbers
add = lambda a, b: a + b
# Function call
sum_value = add(5, 3)
print(sum_value)  # Output: 8