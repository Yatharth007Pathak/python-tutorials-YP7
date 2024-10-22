# Armstrong number

def is_armstrong(number):
    # Convert number to string to easily iterate over digits
    num_str = str(number)
    
    # Get the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == number

# Get input from the user
try:
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")


'''
An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
'''

'''
Here's a detailed explanation of the code:

def is_armstrong(number): defines a function named is_armstrong that takes a single parameter number, which is expected to be an integer.

num_str = str(number) converts the integer number to a string, allowing easy iteration over its digits.

num_digits = len(num_str) calculates the number of digits in the number by finding the length of the string num_str.

sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) calculates the sum of each digit raised to the power of the number of digits.
This is done using a generator expression:

int(digit) converts each character digit back to an integer.
int(digit) ** num_digits raises this integer to the power of num_digits.
sum(...) computes the total sum of these powered digits.
return sum_of_powers == number checks if the computed sum of powered digits is equal to the original number. 
If they are equal, the function returns True, indicating that number is an Armstrong number; otherwise, it returns False.

try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

if is_armstrong(num): calls the is_armstrong function with the user-provided number num and checks if the result is True.

print(f"{num} is an Armstrong number.") prints a message indicating that the number is an Armstrong number if the condition is true.

else: handles the case where the number is not an Armstrong number.

print(f"{num} is not an Armstrong number.") prints a message indicating that the number is not an Armstrong number if the condition is false.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''