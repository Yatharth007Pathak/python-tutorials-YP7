# Fibonacci Sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to print: "))
fibonacci(n)

'''
Here's a line-by-line explanation of the code:

def fibonacci(n): defines a function named fibonacci that takes a single parameter n, which represents the number of Fibonacci numbers to print.

a, b = 0, 1 initializes two variables a and b to 0 and 1, respectively. These variables represent the first two numbers in the Fibonacci sequence.

for _ in range(n): starts a loop that iterates n times, where each iteration corresponds to generating and printing the next Fibonacci number.

print(a, end=' ') prints the current value of a, followed by a space, without moving to a new line. 
This keeps the numbers on the same line, separated by spaces.

a, b = b, a + b updates the values of a and b for the next iteration. 
a is set to the current value of b, and b is set to the sum of the current values of a and b. 
This effectively shifts the sequence forward by one step.

n = int(input("Enter the number of Fibonacci numbers to print: ")) prompts the user to enter the number of Fibonacci numbers they want to print, 
converts this input to an integer, and stores it in the variable n.

fibonacci(n) calls the fibonacci function with the user-provided value of n to print the Fibonacci sequence.
'''