"""
In Object-Oriented Programming (OOP), exception handling can be integrated using the 
try, except, and finally blocks to manage errors gracefully. Here's how each part works:
"""

class Calculator:
    def divide(self, a, b):
        try:
            result = a / b                                    # Attempt to perform division
            return result                                     # Return the result if division is successful
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")            # Handle the division by zero exception
        finally:
            print("Division operation attempted.")            # This block will always execute, regardless of whether an exception occurred

# Create an instance of Calculator
calc = Calculator()

# Perform division operation
result = calc.divide(10, 2)                                   # No exception, division is successful
print(f"Result: {result}")                                    # Output: Result: 5.0

# Perform a division by zero operation
result = calc.divide(10, 0)                                   # Raises ZeroDivisionError, handled by except block
print(f"Result: {result}")                                    # Output: Result: None


'''
This code defines a Calculator class that includes a method for performing division operations with error handling. Let's break it down:

class Calculator:
This line defines a class named Calculator.

def divide(self, a, b):
This line defines a method divide within the Calculator class. The method takes three parameters: 
self (which refers to the instance of the class), a (the numerator), and b (the denominator).

try:
The try block is where you attempt the division operation. If an error occurs, the program will jump to the corresponding except block.

result = a / b
This line attempts to divide a by b and assigns the result to the variable result. If b is zero, this will raise a ZeroDivisionError.

return result
If the division is successful (i.e., no exception is raised), the method returns the result.

except ZeroDivisionError:
This block catches the ZeroDivisionError if b is zero, preventing the program from crashing.

print("Error: Cannot divide by zero.")
If a ZeroDivisionError is caught, this line prints an error message indicating that division by zero is not allowed.

finally:
The finally block contains code that will always execute, whether an exception was raised or not. It's useful for clean-up actions or logging.

print("Division operation attempted.")
This line prints a message indicating that a division operation was attempted, regardless of whether it was successful or not.

Creating an Instance and Performing Division
calc = Calculator()
This line creates an instance of the Calculator class named calc.

result = calc.divide(10, 2)
This line calls the divide method on the calc object, attempting to divide 10 by 2. 
Since 2 is not zero, the division is successful, and result will be 5.0.

print(f"Result: {result}")
This prints the result of the division, which is 5.0.

result = calc.divide(10, 0)
This line calls the divide method again, this time attempting to divide 10 by 0. 
Since division by zero is not allowed, a ZeroDivisionError is raised, the error message is printed, 
and result is None (as nothing is returned when the error occurs).

print(f"Result: {result}")
This prints the result of the second division attempt. Since the division failed due to a zero denominator, result will be None.
'''