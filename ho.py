# Product of Digits

def product_of_digits(n):
    if n == 0:
        return 1
    else:
        return n % 10 * product_of_digits(n // 10)

n = int(input("Enter n: "))
print(product_of_digits(n))

'''
Here's a detailed breakdown of the code:

def product_of_digits(n): defines a function named product_of_digits that takes a single parameter n, 
which is expected to be a non-negative integer.

if n == 0: checks if n is 0. If so, the function returns 1. This is because multiplying by 0 will yield 0, 
and for the purpose of calculating the product of digits, returning 1 when n is 0 is a sensible base case.

else: handles the case where n is not 0.

return n % 10 * product_of_digits(n // 10) calculates the product of the digits of n using recursion:

n % 10 extracts the last digit of n.
n // 10 removes the last digit of n.
The function recursively calls product_of_digits(n // 10) to compute the product of the remaining digits.
The result is the product of the last digit and the product of the remaining digits.
n = int(input("Enter n: ")) prompts the user to enter a non-negative integer, converts this input to an integer, and stores it in the variable n.

print(product_of_digits(n)) calls the product_of_digits function with the user-provided value of n and prints the result.
'''