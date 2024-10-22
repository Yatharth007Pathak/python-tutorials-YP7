# Sum of Digits

def sum_of_digits(n):

    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    else:
        return n % 10 + sum_of_digits(n // 10)

n = int(input("Enter n: "))
print(sum_of_digits(n))

'''
Here's a detailed explanation of the code:

def sum_of_digits(n): defines a function named sum_of_digits that takes a single parameter n, which is expected to be a non-negative integer.

if n == 0: checks if n is 0. If so, the function returns 0, because the sum of the digits of 0 is 0.

else: handles the case where n is not 0.

return n % 10 + sum_of_digits(n // 10) calculates the sum of the digits of n using recursion:

n % 10 extracts the last digit of n.
n // 10 removes the last digit of n.
The function recursively calls sum_of_digits(n // 10) to find the sum of the remaining digits.
The result is the sum of the last digit and the sum of the remaining digits.
n = int(input("Enter n: ")) prompts the user to enter a non-negative integer, converts this input to an integer, and stores it in the variable n.

print(sum_of_digits(n)) calls the sum_of_digits function with the user-provided value of n and prints the result.
'''