# Factorial Calculation

def factorial(n):

    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    else:
        return n * factorial(n-1)

n = int(input("Enter n: "))
print(factorial(n))


'''
line-by-line breakdown of the code:

def factorial(n): defines a function named factorial that takes a single parameter n.

if n == 0: checks if the value of n is 0. This is the base case for the recursion.

return 1 returns 1 if n is 0, which is the factorial of 0 by definition.

else: is executed if n is not 0.

return n * factorial(n-1) returns the product of n and the result of the factorial function called with n-1. 
This recursive call continues until n reaches 0.

n = int(input("Enter n: ")) prompts the user to enter a number, converts the input to an integer, and stores it in the variable n.

print(factorial(n)) calls the factorial function with the user-provided value of n and prints the result.
'''