# Fibonnaci number and fibonacci sequence

def fibonacci(n):

    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Recursive case: sum of the two preceding numbers
    else:        
        return fibonacci(n - 1) + fibonacci(n - 2)


# Testing the Fibonacci function

# Prints the fibonnaci number
n = int(input("Enter n: "))
print(fibonacci(n))  

# Prints the fibonnaci sequence
for i in range(1, n+1):
    print(fibonacci(i), end = " ")

'''
Here's a breakdown of the code:

def fibonacci(n):: This line defines a function named fibonacci that takes one argument, n. 
The function will return the Fibonacci number at position n.

# Base cases: This comment indicates that the next few lines handle the base cases of the Fibonacci sequence.

if n == 1:: This line checks if n is 1. If so, the function returns 0 because the first Fibonacci number is 0.

return 0: If n is 1, this line returns 0, which is the first Fibonacci number.

elif n == 2:: This line checks if n is 2. If so, the function returns 1 because the second Fibonacci number is 1.

return 1: If n is 2, this line returns 1, which is the second Fibonacci number.

# Recursive case: sum of the two preceding numbers: This comment explains that the next part of the code 
handles the recursive calculation for positions greater than 2.

else:: This line is executed if n is greater than 2. It triggers the recursive calculation of the Fibonacci number 
by summing the two preceding numbers in the sequence.

return fibonacci(n - 1) + fibonacci(n - 2): This line returns the sum of the Fibonacci numbers at positions n-1 and n-2, 
effectively calculating the Fibonacci number at position n using the recursive formula.

# Testing the Fibonacci function: This comment indicates that the next section of the code is for testing the fibonacci function

n = int(input("Enter n: ")): This line prompts the user to enter a value for n, 
converts the input string to an integer, and stores it in the variable n.

print(fibonacci(n)): This line prints the Fibonacci number at position n by calling the fibonacci function with the user-provided n.

# Prints the Fibonacci sequence: This comment indicates that the following lines of code 
will print the entire Fibonacci sequence up to position n.

for i in range(1, n+1):: This line initiates a loop that iterates from 1 through n, inclusive, to print each Fibonacci number in the sequence.

print(fibonacci(i), end = " "): Within the loop, this line calls the 
fibonacci function for each position i and prints the corresponding Fibonacci number, 
followed by a space (end = " "), effectively displaying the sequence on a single line.
'''