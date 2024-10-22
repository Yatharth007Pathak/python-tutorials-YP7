# Check if a Number is Perfect

def is_perfect(number):
    if number < 1:
        return False
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

# Example usage
try:
    num = int(input("Enter a number: "))
    if is_perfect(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")


# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself)

'''
Here's a detailed breakdown of the code:

def is_perfect(number): defines a function named is_perfect that takes a single parameter number, which is expected to be an integer.

if number < 1: checks if the number is less than 1. Since perfect numbers are positive integers greater than 0, 
the function returns False for numbers less than 1.

divisors_sum = sum(i for i in range(1, number) if number % i == 0):

range(1, number) generates numbers from 1 to number - 1.
if number % i == 0 checks if i is a divisor of number.
i for i in range(1, number) creates a generator that includes only the divisors.
sum(...) calculates the sum of these divisors.
return divisors_sum == number checks if the sum of the proper divisors (divisors_sum) is equal to the original number. 
If they are equal, the number is a perfect number, and the function returns True; otherwise, it returns False.

try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

if is_perfect(num): calls the is_perfect function with num as the argument and checks if the result is True.

print(f"{num} is a perfect number.") prints a message indicating that the number is a perfect number if the condition is true.

else: handles the case where the number is not a perfect number.

print(f"{num} is not a perfect number.") prints a message indicating that the number is not a perfect number if the condition is false.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''