# Convert a Binary Number to Decimal

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Example usage
binary_str = input("Enter a binary number: ")
try:
    print(f"The decimal equivalent of binary {binary_str} is {binary_to_decimal(binary_str)}.")
except ValueError:
    print("Please enter a valid binary number.")

'''
Here's a detailed explanation of the code:

def binary_to_decimal(binary_str): defines a function named binary_to_decimal that takes a single parameter binary_str, 
which is expected to be a string representing a binary number.

return int(binary_str, 2) converts the binary string to a decimal integer:
int(binary_str, 2) converts the string binary_str from base 2 (binary) to a base 10 (decimal) integer.
binary_str = input("Enter a binary number: ") prompts the user to enter a binary number and stores this input in the variable binary_str.

try: starts a block that attempts to execute code that might raise an exception.

print(f"The decimal equivalent of binary {binary_str} is {binary_to_decimal(binary_str)}."):

Calls the binary_to_decimal function with binary_str as the argument.
Prints the decimal equivalent of the binary number.
except ValueError: catches any ValueError that occurs if the input is not a valid binary number.

print("Please enter a valid binary number.") prints an error message if the user input is not a valid binary number 
(e.g., contains characters other than 0 and 1).
'''