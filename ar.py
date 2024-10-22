num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

sum_result = num1 + num2

print(f"The sum of {num1} and {num2} is: {sum_result}")
print("The sum of", num1, "and", num2, "is:", sum_result)


'''
input("Enter the first number: ") and input("Enter the second number: "): These lines prompt the user to enter 2 numbers and store them as strings.
int(num1) and int(num2): Convert the input strings to integers.
num1 + num2: Adds the two integers together.
'''

"""
print(f"The sum of {num1} and {num2} is: {sum_result}"): Prints the result of the addition.
f"...": The f before the opening quotation mark indicates that the string is an f-string. 
Inside the string, we can include expressions in curly braces {}. 
These expressions will be evaluated and replaced with their values when the string is printed.
"The sum of ": This is a plain string that will be printed as is.
{num1}: This is an expression inside curly braces. It will be replaced by the value of the variable num1.
" and ": Another plain string.
{num2}: This will be replaced by the value of num2.
" is: ": Plain string.
{sum_result}: This will be replaced by the value of sum_result.
"""

'''
print("The sum of", num1, "and", num2, "is", sum_result): Prints the result of the addition.
"The sum of": This is a string literal that will be printed as is.
num1: This is a variable that holds a value (e.g., an integer or a float). The value of num1 will be printed in place of the variable name.
"and": Another string literal.
num2: Similar to num1, this will be replaced by the value of num2.
"is": Another string literal.
sum_result: This will be replaced by the value of sum_result, which should be the sum of num1 and num2.
Commas (,) are used to separate the different arguments that we want to print. 
Each of these arguments can be a string, variable, or even an expression.
Automatic Spacing: When using commas to separate arguments in the print() function, 
Python automatically adds spaces between the arguments in the output. So, we don't need to manually add spaces in the strings.
'''