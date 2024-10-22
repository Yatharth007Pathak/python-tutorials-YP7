# Numbers from n to 1

def printNto1(n):

    # Base case
    if n == 0:
        return
    
    # Recursive case
    print(n)
    printNto1(n-1)

n = int(input("Enter n: "))
printNto1(n)

'''
Here's a line-by-line breakdown:

def printNto1(n):: This line defines a function named printNto1 that takes one argument, n. 
This function will be responsible for printing numbers from n down to 1.

if n == 0:: This line checks if the value of n is 0. If n is 0, it means the function has reached the base case, and no further action is needed.

return: If the previous condition (n == 0) is true, this line stops the function's execution, effectively ending the recursive process.

print(n): If n is not 0, this line prints the current value of n.

printNto1(n-1): This line calls the printNto1 function recursively with the argument n-1, 
which continues the process of printing the next lower number until it reaches 1.

n = int(input("Enter n: ")): This line prompts the user to enter a value for n. 
The input is taken as a string, converted to an integer, and stored in the variable n.

printNto1(n): This line calls the printNto1 function with the user's input, initiating the process of printing numbers from n down to 1.
'''