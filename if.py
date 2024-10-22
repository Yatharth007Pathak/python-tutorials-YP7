# Check if a Number is Armstrong

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

# Example usage
try:
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")

'''
Here's a detailed explanation of the code:

def is_armstrong_number(number): defines a function named is_armstrong_number that takes a single parameter number, which is the number to check.

num_str = str(number) converts number to a string and stores it in num_str. This allows easy iteration over each digit.

num_digits = len(num_str) calculates the number of digits in the number by finding the length of num_str.

sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) computes the sum of each digit raised to the power of the number of digits:
int(digit) converts each character in num_str back to an integer.
int(digit) ** num_digits raises the digit to the power of num_digits.
sum(...) adds up these powered values for all digits.
return sum_of_powers == number checks if the sum of the powered digits is equal to the original number. 
If it is, the number is an Armstrong number; otherwise, it is not.

try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

if is_armstrong_number(num): calls the is_armstrong_number function with num as the argument and checks if the result is True.

print(f"{num} is an Armstrong number.") prints a message indicating that the number is an Armstrong number if the condition is true.

else: handles the case where the number is not an Armstrong number.

print(f"{num} is not an Armstrong number.") prints a message indicating that the number is not an Armstrong number if the condition is false.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''