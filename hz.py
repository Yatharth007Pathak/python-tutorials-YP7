# Find the Largest Prime Factor

def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

# Example usage
try:
    num = int(input("Enter a number: "))
    print(f"The largest prime factor of {num} is {largest_prime_factor(num)}.")
except ValueError:
    print("Please enter a valid integer.")

'''
Here's a detailed explanation of the code:

def largest_prime_factor(n): defines a function named largest_prime_factor that takes a single parameter n, which is expected to be an integer.

factor = 2 initializes the variable factor to 2, the smallest prime number.

while factor * factor <= n: starts a loop that continues as long as factor * factor is less than or equal to n. 
This condition ensures that the loop only checks factors up to the square root of n, which is sufficient to find all prime factors.

if n % factor: checks if n is not divisible by factor (i.e., n % factor is not zero). 
If n is not divisible by factor, it means factor is not a prime factor of n.

factor += 1 increments factor by 1 to check the next potential factor.

else: handles the case where n is divisible by factor.

n //= factor divides n by factor using integer division and updates n with the result. 
This effectively removes all occurrences of factor from n.

return n returns the largest remaining value of n after the loop finishes. 
At this point, n is either 1 or the largest prime factor of the original number.

try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

print(f"The largest prime factor of {num} is {largest_prime_factor(num)}.") 
calls the largest_prime_factor function with num as the argument and prints the largest prime factor of the number.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''