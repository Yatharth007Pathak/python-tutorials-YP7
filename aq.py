'''
Type casting in programming refers to the process of converting a variable from one data type to another. 
This is often necessary when you need to perform operations between different types or when you need 
to use a variable in a context that requires a specific type.
'''

''' Implicit Casting (Automatic/Coercion):
The conversion is automatically handled by the programming language.
Typically occurs when you mix types that the language can convert without losing data. '''
num = 10                # Integer
result = num + 5.0      # 5.0 is a float
print(result)
# result is implicitly cast to float: 15.0

''' Explicit Casting (Manual/Type Conversion):
The programmer explicitly converts the type using functions or methods.
Necessary when converting between types that might lose information or when implicit conversion is not possible. '''
num_str = "123"         # String
num = int(num_str)      # Convert to integer
print(num + 10)         # 133

num = 100
num_str = str(num)      # Converts integer to string
print(num)

print(int("123"))       # Converts string to integer
print(float("123"))     # Converts string to float
print(str(123))         # Converts integer to string
print(int(3.14))        # Converts float to integer

float_str = "12.34"
num_float = float(float_str)  # Converts string to float
print(float_str)

num_float = 9.99
num_int = int(num_float)  # Converts float to integer (truncates decimal part)
print(num_int)

''' To perform type casting where we input something (like a string) and turn it into an integer in Python, we can use the int() function. '''
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    print(f"The number you entered is: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

age = int(input("Enter your age: "))
print(age)
print(type(age))


"""
Considerations:
Data Loss: Converting a float to an integer will lose the decimal part.
Errors: Trying to convert an invalid string to a number (e.g., int("abc")) will raise an error.
Type casting is crucial for ensuring that operations between different data types are valid and perform as expected.
"""