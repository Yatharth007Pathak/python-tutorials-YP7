'''
Basic Exception Handling

The try block contains the code that might raise an exception. It is used to wrap the code that you want to monitor for errors.

The except block handles the exception if one occurs. 
We can specify the type of exception you want to catch, and optionally, you can have multiple except blocks for different exceptions.

The finally block is executed no matter what—whether an exception was raised or not. 
It is typically used for clean-up actions, such as closing files or releasing resources.
'''

try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))           # Attempt to convert user input to an integer
    result = 10 / number                           # Attempt to divide 10 by the entered number
    print("Result is", result)             # Print the result of the division
except ZeroDivisionError:
    # Code to handle division by zero
    print("Error: Cannot divide by zero.")  # Print an error message if division by zero occurs
except ValueError:
    # Code to handle invalid input (non-integer)
    print("Error: Invalid input. Please enter a valid number.")  # Print an error message for invalid input
finally:
    # Code that will always execute, regardless of whether an exception occurred or not
    print("Execution completed.")  # Print a message indicating the end of execution

'''

This code demonstrates the use of exception handling in Python to manage potential errors that may occur during the execution of a program. 
Here's a line-by-line breakdown of the code:

try:
This begins a try block where you place the code that might raise an exception. The program will attempt to execute this code.

number = int(input("Enter a number: "))
This line prompts the user to input a number. 
The input() function captures the user's input as a string, and the int() function attempts to convert this string into an integer. 
If the user enters something that cannot be converted to an integer (e.g., a letter or symbol), this will raise a ValueError.

result = 10 / number
This line attempts to divide 10 by the number entered by the user. 
If the user enters 0, this will raise a ZeroDivisionError because division by zero is not allowed in mathematics.

print("Result is", result)
If no exceptions are raised, this line prints the result of the division.

except ZeroDivisionError:
This block of code will execute if a ZeroDivisionError is raised in the try block (e.g., if the user entered 0). 
It allows the program to handle the error gracefully instead of crashing.

print("Error: Cannot divide by zero.")
This line prints an error message if the division by zero occurs.

except ValueError:
This block will execute if a ValueError is raised in the try block (e.g., if the user enters a non-integer value like a letter or symbol).

print("Error: Invalid input. Please enter a valid number.")
This line prints an error message if the user input is invalid and cannot be converted to an integer.

finally:
This block will always execute, regardless of whether an exception occurred or not. It is useful for cleaning up resources or finalizing tasks.

print("Execution completed.")
This line prints a message indicating that the execution of the code block is completed, whether an exception was raised or not.
'''