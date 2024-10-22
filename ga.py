"""
In Python, a nested function is a function that is defined inside another function. Nested functions are also known as inner functions. 
They are useful for encapsulating functionality that is only relevant to the enclosing function 
and can help to keep your code organized and maintainable.

Key Concepts of Nested Functions

Scope:
The inner function is only accessible within the scope of the outer function. 
This means we cannot call the inner function directly from outside the outer function.
The inner function can access variables from the enclosing function's scope.

Encapsulation:
Inner functions can help encapsulate functionality that is only relevant to the outer function, preventing it from being exposed globally.
Useful for organizing code and keeping helper functions private.

Closures:
A nested function can capture and remember the values of variables from its enclosing scope. This feature is known as a closure.
"""

def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + 5

result = outer_function(4)
print(result)  # Output: 21

'''
In this example:
inner_function is defined inside outer_function.
inner_function is used within outer_function to perform a calculation.
'''

'''
Let's break down the code line by line:

def outer_function(x):
This line defines a function named outer_function that takes one parameter, x. The function can be called with a value passed to x.

    def inner_function(y):
Inside outer_function, another function called inner_function is defined. inner_function takes one parameter, y. 
This is a nested function, meaning it is defined within another function and can be accessed only within the scope of outer_function.

        return y * y
This line specifies the return value of inner_function.
This line is the body of inner_function. It takes the input y and returns its square (y * y).

    return inner_function(x) + 5
This line is the return statement of outer_function. 
It calls inner_function with x as its argument (so y becomes x within inner_function), squares x, and then adds 5 to the result. 
The final value is returned by outer_function.

result = outer_function(4)
Here, outer_function is called with the argument 4. The result of this function call is stored in the variable result.

print(result)  # Output: 21
The print function is used to output the value of result. The comment # Output: 21 suggests the expected output is 21.

Execution Breakdown
Call outer_function(4): The function outer_function is called with x = 4.
Call inner_function(4): Inside outer_function, inner_function is called with y = 4.
Return 16 from inner_function(4): inner_function calculates 4 * 4 and returns 16.
Return 21 from outer_function(4): The outer_function adds 5 to 16, resulting in 21, and returns 21.
Store 21 in result: The value 21 is stored in the variable result.
Print 21: The value of result, which is 21, is printed to the console.
So, the final output of the code is 21.
'''