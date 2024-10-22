""" In Python, the input() function is used to take user input from the console.
It allows us to prompt the user for information, which is then read as a string """

user_input = input("Please enter something: ")
print("You entered:", user_input)
'''
input("Please enter something: "): This displays the prompt message to the user and waits for them to type something and press Enter. 
The input is captured as a string.
user_input: Stores the string that the user typed.
print("You entered:", user_input): Prints the value of user_input.
'''

number_input = input("Please enter a number: ")
number = int(number_input)
print("You entered the number:", number)
# If we want to take an integer input, we need to convert the input string to an integer using int()

try:
    user_input_ = input("Please enter a number: ")
    number_ = int(user_input_)
    print("You entered the number:", number_)
except ValueError:
    print("That's not a valid number.")
# To handle cases where the user might enter something that cannot be converted to an integer, we can use a try/except block



""" In Python, the print() function is used to output data to the console.
It's one of the most frequently used functions for displaying information, debugging, and providing feedback to the user. """

print("Hello, World!")
# print("Hello, World!"): This prints the string "Hello, World!" to the console.

print("A", "B", "C", sep="-")
# By default, print() separates items with a space. We can change this using the sep parameter

print("Hello", end=", ")
print("World")
# By default, print() ends with a newline character. We can change this using the end parameter

name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
# We can format strings using f-strings (formatted string literals)

print("Name: {}, Age: {}".format(name, age))
# Alternatively, we can use the format() method

print("First line\nSecond line\nThird line")
# To print text with multiple lines, we can include newline characters \n within the string



'''
input() always returns a string: Even if the user inputs a number, it is read as a string, 
so we need to convert it to the appropriate type if necessary.
No input() function in Python 2: In Python 2, use raw_input() for string inputs, 
and input() to evaluate expressions (though it's generally better to use raw_input()).
The input() function is versatile and commonly used for interactive programs.

print(): Outputs data to the console.
sep parameter: Customizes the separator between items.
end parameter: Customizes what is printed at the end of the output (default is newline).
String formatting: Use f-strings or format() method for formatting output.
The print() function is a fundamental tool in Python for displaying and debugging information.
'''