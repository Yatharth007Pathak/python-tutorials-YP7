"""
Nested for loops in Python are used to perform iterations within iterations, allowing us to handle multidimensional data structures, 
such as lists of lists, or to execute operations that require multiple levels of looping.
"""

# Outer loop for the first number in the multiplication
for i in range(1, 11):
    # Inner loop for the second number in the multiplication
    for j in range(1, 11):
        # Calculate and print the product
        product = i * j
        print(f"{i} x {j} = {product}")
    # Print a blank line to separate rows
    print()


# nested for loops to print a multiplication table from 1 to 10.

'''
Explanation:
Outer Loop (for i in range(1, 11):): This loop iterates through numbers 1 to 10. 
Each iteration represents one row of the multiplication table.

Inner Loop (for j in range(1, 11):): For each iteration of the outer loop, this inner loop iterates through numbers 1 to 10. 
It calculates and prints the product of i and j.

Print Statement (print(f"{i} x {j} = {product}")): This statement prints the multiplication result for each pair of numbers.

Blank Line (print()): This adds a blank line after each row of the table for better readability.
'''