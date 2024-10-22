# Pass by value

def AddOne(x):
    x = x + 1
    print("Inside function:", x)

x = 5
AddOne(x)
print("Outside function:", x)


'''
Here's a line-by-line breakdown of the code:

def AddOne(x):
This line defines a function named AddOne that takes one argument, x. This function will modify x and print its value inside the function.

A function in Python is a block of code that only runs when it is called. We can pass data, known as parameters, into a function. 
A function can return data as a result.

    x = x + 1
This line is inside the function and adds 1 to the value of x. The result is then stored back in x.
This operation modifies the value of x within the function, it doesn't affect the value of x outside the function.

    print("Inside function:", x)
This line prints the string "Inside function:" followed by the current value of x after it has been incremented inside the AddOne function. 
This helps us see the value of x after it has been incremented.
The print function is used to output text and variables.

x = 5
This line assigns the value 5 to the variable x.
This x is outside the function and is independent of the x inside the function.

AddOne(x)
This line calls the AddOne function and passes the value of x (which is 5) as an argument.
Inside the function, the value of x becomes 6 (since 5 + 1 = 6) and is printed as "Inside function: 6".
However, this does not change the value of x outside the function.

print("Outside function:", x)
This line prints the string "Outside function:" followed by the value of x outside the function. 
Since the x inside the function is a local variable (meaning its scope is limited to the function), 
Since the x outside the function was not modified by AddOne, it remains 5.
This will print "Outside function: 5".

Key Points:
The function modifies x only within its own scope.
The value of x outside the function remains unchanged because the modification inside the function does not affect the global variable x.
'''