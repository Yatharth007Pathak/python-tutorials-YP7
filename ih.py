# Numbers from 1 to n

def print1toN(n):

    # Base case
    if n == 0:
        return
    
    # Recursive case
    print1toN(n-1)
    print(n)

n = int(input("Enter n: "))
print1toN(n)

'''
Here's a breakdown of the code line by line:

def print1toN(n):: This line defines a function named print1toN that takes one argument, n. 
The function will print numbers starting from 1 up to n.

if n == 0:: This line checks if the value of n is 0. If n is 0, the function reaches its base case, meaning there are no numbers to print.

return: If the previous condition (n == 0) is true, this line stops the function's execution, effectively ending the recursion.

print1toN(n-1): If n is not 0, this line calls the print1toN function recursively with the argument n-1. 
This step keeps reducing n by 1, allowing the function to first reach the smallest value (1) before printing.

print(n): After the recursive call completes, this line prints the current value of n. 
Since the function unwinds after reaching the base case, this print statement outputs the numbers in ascending order.

n = int(input("Enter n: ")): This line prompts the user to enter a value for n, 
converts the input string to an integer, and stores it in the variable n.

print1toN(n): This line calls the print1toN function with the user's input, starting the process of printing numbers from 1 to n.
'''