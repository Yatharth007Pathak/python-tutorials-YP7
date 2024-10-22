# Handling Division by Zero
# This example handles a division by zero error and uses the finally block to execute code regardless of whether an exception occurred.

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

'''
try: Attempts to divide by zero.
except: Catches the ZeroDivisionError and prints an error message.
finally: Always executes, printing "Execution completed."
'''

'''
This code snippet demonstrates the use of exception handling in Python to manage an error that occurs when attempting to divide by zero.
Let's break it down step by step:

try:
This begins a try block, where you place the code that might raise an exception. The program will attempt to execute the code inside this block.

numerator = 10
This line assigns the value 10 to the variable numerator.

denominator = 0
This line assigns the value 0 to the variable denominator.

result = numerator / denominator
This line attempts to divide numerator by denominator. 
Since the denominator is 0, this operation will raise a ZeroDivisionError, as division by zero is mathematically undefined.

except ZeroDivisionError:
This block will execute if a ZeroDivisionError is raised in the try block. 
It allows the program to handle the division by zero error gracefully, instead of crashing.

print("Error: Division by zero is not allowed.")
This line prints an error message indicating that division by zero is not allowed.

finally:
This block will always execute, regardless of whether an exception was raised or not. 
The finally block is used for any cleanup code or actions that should happen after the try and except blocks.

print("Execution completed.")
This line prints a message indicating that the execution of the code block is completed, no matter the outcome of the try block.
'''