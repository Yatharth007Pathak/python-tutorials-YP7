# Conditional statements

# Python program that demonstrates the use of if and if-else statements.
num = float(input("Enter a num: "))
if num > 0:
    print("The num is positive.")
elif num < 0:
    print("The num is negative.")
else:
    print("The num is zero.")

# Python program that demonstrates the use of nested if-else statements.
number = float(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
else:
    if number > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# Python program that demonstrates the use of match-case statements.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operator = input("Enter operator: ")
match operator:
    case "+":
        print("Sum is", num1 + num2)
    case "-": 
        print("Difference is", num1 - num2)
    case "*":
        print("Product is", num1 * num2)
    case "/":
        print("Division is", num1 + num2)
    case _:
        print("Enter a valid operator")

# Python program that demonstrates the use of ternary operator
age = int(input("Enter age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)

# Python program that demonstrates the use of else if ladder (also known as elif in Python)
number = int(input("Enter a number: "))
if number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")
elif number > 0 and number <= 10:
    print("The number is between 1 and 10.")
elif number > 10 and number <= 100:
    print("The number is between 11 and 100.")
else:
    print("The number is greater than 100.")
