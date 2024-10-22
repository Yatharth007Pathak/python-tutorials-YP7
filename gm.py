x = 50
def func(x):
    x = 2
func(x)
print("x is now", x)

'''
Let's break down the code step by step:

x = 50:
This line assigns the value 50 to the variable x. At this point, x is a global variable.

def func(x)::
This defines a function named func that takes one argument, also named x. This x is a local variable specific to the function.

x = 2 (inside func):
Within the function func, the local variable x is assigned the value 2. 
This does not affect the global variable x; it only changes the local x within the function's scope.

func(x):
This calls the function func with the global variable x (which is 50) as an argument.
Inside the function, x becomes 2, but this change is local to the function and does not affect the global variable x.

print("x is now", x):
This prints the value of the global variable x, 
which remains unchanged at 50 because the assignment inside func did not modify the global variable.

The output of the code will be: x is now 50

Key Concepts
Global vs. Local Variables: x inside func is a local variable, separate from the global x.
Scope: Changes to x inside func do not affect the global x because they occur in a different scope.
'''