# Prime Check

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter n: "))
print(is_prime(n))

'''
Here's a detailed breakdown of the code:

def is_prime(n): defines a function named is_prime that takes a single parameter n.

if n <= 1: checks if the value of n is less than or equal to 1. 
Numbers less than or equal to 1 are not prime, so the function returns False in this case.

for i in range(2, n): starts a loop with i ranging from 2 up to, but not including, n. 
This loop checks if n is divisible by any number between 2 and n-1.

if n % i == 0: checks if n is divisible by i with no remainder. If true, n is not a prime number, so the function returns False.

return True is reached if the loop completes without finding any divisors, indicating that n is a prime number. 
Hence, the function returns True.

n = int(input("Enter n: ")) prompts the user to enter a number, converts the input to an integer, and stores it in the variable n.

print(is_prime(n)) calls the is_prime function with the user-provided value of n and prints the result, 
indicating whether the number is prime or not.
'''