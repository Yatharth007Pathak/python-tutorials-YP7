def outer_function():
    x = 1 # Variable in the outer function

    def inner_function():
        y = 2 # Variable in the inner function
        result = x + y
        return result
    return inner_function()

output = outer_function()
print(output)

'''
Let's break down the code line by line:

def outer_function():
This line defines a function named outer_function that takes no parameters. This function will contain variables and another function within it.

    x = 1  # Variable in the outer function
Inside outer_function, a variable x is created and assigned the value 1. 
This variable x is local to outer_function and can be accessed within this function and any functions defined inside it.

    def inner_function():
A new function named inner_function is defined inside outer_function. 
This is a nested function that can access variables from its enclosing scope, which is outer_function.

        y = 2  # Variable in the inner function
Inside inner_function, a variable y is created and assigned the value 2. 
This variable is local to inner_function and cannot be accessed outside of it.

        result = x + y
The variable result is assigned the sum of x and y. 
Here, x is accessed from the outer function's scope, while y is from the inner function's scope.

        return result
The inner_function returns the value of result to the caller. This value is the sum of x and y.

    return inner_function()
The outer_function calls inner_function and returns its result. 
Since inner_function returns the sum of x and y, outer_function will return this sum as its own result.

output = outer_function()
Here, outer_function is called, and its result (the sum of x and y) is stored in the variable output.

print(output)
The print function is used to output the value of output to the console. This will display the sum of x and y (which is 3) on the screen.

Execution Breakdown
Call outer_function(): The function outer_function is called.
Assign x = 1: Within outer_function, the variable x is assigned the value 1.
Define inner_function(): The function inner_function is defined, but not yet executed.
Call inner_function(): inner_function is called from within outer_function.
Assign y = 2: Within inner_function, the variable y is assigned the value 2.
Compute result = x + y: The sum of x and y (which are 1 and 2, respectively) is calculated and stored in result. So, result equals 3.
Return 3 from inner_function(): The value 3 is returned from inner_function.
Return 3 from outer_function(): The value 3 is returned from outer_function to the caller.
Store 3 in output: The value 3 is stored in the variable output.
Print 3: The value of output (3) is printed to the console.
So, the final output of the code is 3.
'''