"""
Closures occur when an inner function captures the state of its enclosing function. 
This allows the inner function to remember the values of variables from the outer function even after the outer function has finished execution.
"""

def outer_function(x):
    def inner_function(y):
        return x + y  # Inner function uses `x` from the outer function
    return inner_function

closure_function = outer_function(10)
print(closure_function(5))  # Output: 15

'''
In this example:
inner_function captures the value of x from outer_function.
Even though outer_function has finished execution, closure_function still remembers the value of x.
'''

'''
Let's break down this code line by line:

def outer_function(x):
This line defines a function named outer_function that takes one parameter, x. 
The function will return another function, which can later be called.

    def inner_function(y):
Inside outer_function, another function called inner_function is defined. This function takes one parameter, y. 
It has access to x because x is defined in the outer function's scope.

        return x + y  # Inner function uses `x` from the outer function
The inner_function returns the sum of x and y. 
Here, x is not passed directly to inner_function; instead, it is accessed from the scope of outer_function. 
This concept is known as a closure, where inner_function "remembers" the value of x even after outer_function has finished execution.

    return inner_function
The outer_function returns the inner_function itself, not the result of calling inner_function. 
This means outer_function returns a function that can be called later, with x already set to the value passed into outer_function.

closure_function = outer_function(10)
Here, outer_function is called with the argument 10. This sets x = 10 within outer_function. 
The returned inner_function is stored in the variable closure_function. 
At this point, closure_function is essentially inner_function with x bound to 10.

print(closure_function(5))  # Output: 15
The closure_function is called with the argument 5, which sets y = 5 in inner_function. 
Since x is already bound to 10, the function returns 10 + 5 = 15. This result is printed, so the output will be 15.

Execution Breakdown
Call outer_function(10): The function outer_function is called with x = 10.
Define inner_function(y): Inside outer_function, the inner_function is defined but not executed.
Return inner_function: The outer_function returns the inner_function, now having x bound to 10. 
This returned function is stored in closure_function.
Call closure_function(5): The closure_function (which is the inner_function returned by outer_function) is called with y = 5.
Compute x + y: Inside inner_function, x is 10 (from outer_function) and y is 5. The function computes 10 + 5 and returns 15.
Print 15: The result 15 is printed to the console.
So, the final output of the code is 15.
'''