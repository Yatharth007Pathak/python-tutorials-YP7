# Summation calculation

def summation(n):
    return sum(range(1, n + 1))

n = int(input("Enter n: "))
result = summation(n)
print(f"Summation till {n}: {result}")


'''
Here's a line-by-line explanation of this code:

def summation(n): defines a function named summation that takes a single parameter n.

return sum(range(1, n + 1)) calculates the sum of all integers from 1 to n. 
The range(1, n + 1) function generates a sequence of integers from 1 to n. The sum() function then adds up these integers and returns the total.

n = int(input("Enter n: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable n.

result = summation(n) calls the summation function with the user-provided value of n and assigns the result to the variable result.

print(f"Summation till {n}: {result}") prints a formatted string that shows the value of n and the computed sum, 
displaying the total sum of integers from 1 to n.
'''