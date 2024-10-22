# Palindrome check of any number

def is_palindrome(number):
    # Convert the number to string
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Get input from the user
try:
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
except ValueError:
    print("Please enter a valid integer.")

'''
Here's a breakdown of the code:

def is_palindrome(number): defines a function named is_palindrome that takes a single parameter number.

num_str = str(number) converts the given number to a string, storing the result in num_str. This allows easy comparison of the number's digits.

return num_str == num_str[::-1] checks if num_str is equal to its reverse. 
The slicing notation [::-1] creates a reversed version of the string. If num_str is the same forwards and backwards, the number is a palindrome.

try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

if is_palindrome(num): calls the is_palindrome function with num and checks if the result is True.

print(f"{num} is a palindrome.") prints a message indicating that the number is a palindrome if the condition is true.

else: handles the case where the number is not a palindrome.

print(f"{num} is not a palindrome.") prints a message indicating that the number is not a palindrome if the condition is false.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''