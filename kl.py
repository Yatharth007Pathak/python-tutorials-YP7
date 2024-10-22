# Input Validation: This example uses exception handling to manage invalid user input.

while True:
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
        break
    except ValueError:
        print("Error: Please enter a valid integer.")
    finally:
        print("Attempt to read a number completed.")

'''
try: Attempts to convert user input to an integer.
except: Catches ValueError if the input is not a valid integer.
finally: Executes after each input attempt, printing a completion message.
'''

'''
This code snippet demonstrates how to repeatedly prompt a user to enter a valid integer until they do so correctly, 
using a combination of a while loop and exception handling. Here's a breakdown of the code:

while True:
This starts an infinite loop. The loop will continue to run until it encounters a break statement, which is used to exit the loop.

try:
This begins a try block, where the code that might raise an exception is placed. 
The program will attempt to execute the code inside this block.

number = int(input("Enter a number: "))
The program prompts the user to enter a number. 
The input() function takes the user's input as a string, and the int() function attempts to convert this string to an integer. 
If the user enters something that cannot be converted to an integer (e.g., letters or symbols), a ValueError will be raised.

print(f"You entered: {number}")
If the conversion to an integer is successful, this line prints the entered number.

break
If the code in the try block runs without raising an exception, the break statement is executed, which exits the while loop. 
This means the loop will stop asking for input once a valid integer is entered.

except ValueError:
This block will execute if a ValueError is raised in the try block (e.g., if the user enters a non-integer value like "abc"). 
It allows the program to handle the error without crashing.

print("Error: Please enter a valid integer.")
If a ValueError is caught, this line prints an error message instructing the user to enter a valid integer. 
The loop then repeats, prompting the user to try again.

finally:
This block will always execute, regardless of whether an exception was raised or not. 
It's useful for any actions that should occur after each attempt to enter a number.

print("Attempt to read a number completed.")
This line is executed every time the loop iterates, printing a message that indicates an attempt to read a number has been completed. 
This happens even if the input was invalid.
'''