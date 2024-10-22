# Calculate the Sum of Squares

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Example usage
try:
    num = int(input("Enter a number: "))
    print(f"The sum of squares of numbers from 1 to {num} is {sum_of_squares(num)}.")
except ValueError:
    print("Please enter a valid integer.")

'''
def sum_of_squares(n): defines a function named sum_of_squares that takes a single parameter n, which is expected to be a positive integer.

return sum(i ** 2 for i in range(1, n + 1)):

range(1, n + 1) generates a sequence of numbers from 1 to n inclusive.
i ** 2 calculates the square of each number i.
sum(...) adds up these squared values.
The function returns the total sum of the squares.
try: starts a block that attempts to execute code that might raise an exception.

num = int(input("Enter a number: ")) prompts the user to enter a number, converts this input to an integer, and stores it in the variable num.

print(f"The sum of squares of numbers from 1 to {num} is {sum_of_squares(num)}."):

Calls the sum_of_squares function with num as the argument.
Prints a message showing the sum of squares of numbers from 1 to num, which is the result returned by sum_of_squares.
except ValueError: catches any ValueError that occurs if the input cannot be converted to an integer.

print("Please enter a valid integer.") prints an error message if the user input is not a valid integer.
'''