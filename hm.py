# Fibonacci Number

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

n = int(input("Enter the term of Fibonacci number to print: "))
print(fibonacci(n))

'''

Here's a breakdown of the code:

def fibonacci(n): defines a function named fibonacci that takes a single parameter n, 
representing the term in the Fibonacci sequence that you want to retrieve.

if n <= 0: checks if n is less than or equal to 0. If so, the function returns the message "Input should be a positive integer." 
because Fibonacci sequence terms are defined only for positive integers.

elif n == 1: checks if n is 1. If so, the function returns 0, which is the first term in the Fibonacci sequence.

elif n == 2: checks if n is 2. If so, the function returns 1, which is the second term in the Fibonacci sequence.

a, b = 0, 1 initializes two variables a and b to 0 and 1, respectively. These variables represent the first two terms in the Fibonacci sequence.

for _ in range(2, n): starts a loop that iterates from 2 to n-1. This loop calculates the Fibonacci term at position n.

a, b = b, a + b updates the values of a and b for the next iteration. 
a is set to the current value of b, and b is set to the sum of the current values of a and b. This shifts the sequence forward by one step.

return b returns the value of b, which holds the Fibonacci term at position n.

n = int(input("Enter the term of Fibonacci number to print: ")) prompts the user to enter a term of the Fibonacci sequence, 
converts this input to an integer, and stores it in the variable n.

print(fibonacci(n)) calls the fibonacci function with the user-provided n and prints the result.
'''