# Find the Greatest Common Divisor (GCD)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f"The GCD of {x} and {y} is {gcd(x, y)}.")
except ValueError:
    print("Please enter valid integers.")

'''
Here's a detailed explanation of the code:

def gcd(a, b): defines a function named gcd that takes two parameters, a and b, 
representing the two numbers for which the Greatest Common Divisor (GCD) is to be computed.

while b: Starts a while loop that continues as long as b is not zero. In Python, while b: is equivalent to while b != 0:. 
The loop will keep running until b becomes zero.

a, b = b, a % b
Inside the loop, this line performs the following:
a, b = b, a % b is a simultaneous assignment that updates the values of a and b.
b is assigned the current value of a % b, which is the remainder when a is divided by b.
a is assigned the old value of b.
This is part of the Euclidean algorithm for finding the GCD, 
where a is repeatedly replaced with b and b is replaced with the remainder of a divided by b.
return a
After the loop exits (i.e., when b becomes zero), a will be the greatest common divisor of the original values of a and b. 
The function returns this value.

try: Starts a try block to handle potential exceptions during user input and function execution.

x = int(input("Enter the first number: ")) prompts the user to enter the first number, 
converts this input to an integer, and stores it in the variable x.

y = int(input("Enter the second number: ")) prompts the user to enter the second number, 
converts this input to an integer, and stores it in the variable y.

print(f"The GCD of {x} and {y} is {gcd(x, y)}.") Calls the gcd function with the user-provided values x and y, 
and prints the result in a formatted string showing the greatest common divisor.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter valid integers.") prints an error message if the user input is not a valid integer.
'''