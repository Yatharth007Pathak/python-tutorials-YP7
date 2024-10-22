# Summation calculation

def summation(n):

    # Base case
    if n == 1:
        return 1
    
    # Recursive case
    else:
        return n + summation(n-1)

n = int(input("Enter n: "))
print(summation(n))


'''
Here's a breakdown of the code:

def summation(n): This line defines a function named summation that takes a single parameter n.

if n == 1: Inside the function, this line checks if the value of n is equal to 1. 
This is the base case for the recursion, which is used to stop the recursion.

return 1 If the condition n == 1 is true, the function returns 1. This provides the terminating condition for the recursive calls.

else: If n is not equal to 1, the execution moves to the else block.

return n + summation(n-1) In the else block, the function returns the value of n plus the result of calling summation with n-1. 
This line effectively adds n to the result of the function for the next smaller integer, thus accumulating the sum through recursive calls.

n = int(input("Enter n: ")) This line prompts the user to enter a value, converts the input to an integer, and stores it in the variable n.

print(summation(n)) Finally, this line calls the summation function with the user-provided value of n and prints the result.
'''