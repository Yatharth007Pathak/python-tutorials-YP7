# Find the Least Common Multiple (LCM)

def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

# Example usage
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f"The LCM of {x} and {y} is {lcm(x, y)}.")
except ValueError:
    print("Please enter valid integers.")

'''

Here's a detailed explanation of the code:

def lcm(a, b): defines a function named lcm that takes two parameters a and b, 
representing the two numbers for which we want to find the least common multiple (LCM).

def gcd(x, y): defines a nested function named gcd that takes two parameters x and y 
and calculates the greatest common divisor (GCD) using the Euclidean algorithm:

while y: runs a loop as long as y is not zero.
x, y = y, x % y updates x to y and y to the remainder of x divided by y.
return x returns the GCD when y becomes zero.
return abs(a * b) // gcd(a, b) calculates and returns the LCM of a and b:

abs(a * b) computes the absolute value of the product of a and b.
// gcd(a, b) divides this product by the GCD of a and b to get the LCM.
try: starts a block that attempts to execute code that might raise an exception.

x = int(input("Enter the first number: ")) prompts the user to enter the first number, 
converts this input to an integer, and stores it in the variable x.

y = int(input("Enter the second number: ")) prompts the user to enter the second number, 
converts this input to an integer, and stores it in the variable y.

print(f"The LCM of {x} and {y} is {lcm(x, y)}.") calls the lcm function with x and y as arguments and prints the LCM of the two numbers.

except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter valid integers.") prints an error message if the user input is not a valid integer.
'''