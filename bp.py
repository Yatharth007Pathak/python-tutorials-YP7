# Get user input
number = int(input("Enter a number: "))

# With ternary operator
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}.")

# Without ternary operator
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"
print(result)

# Python program using a ternary operator (also known as a conditional expression) to determine whether a given number is even or odd



'''
In Python, the ternary operator is a shorthand way to perform a simple conditional assignment or expression. 
It allows us to write compact if-else statements in a single line. 
The general syntax of the ternary operator in Python is:
value_if_true if condition else value_if_false
'''