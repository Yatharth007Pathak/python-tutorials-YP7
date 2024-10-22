"""
Nested while loops in Python work similarly to nested for loops but use the while loop construct instead. 
They are used when the number of iterations is not known beforehand and you want to continue iterating based on a condition.
"""

# Initialize the starting number for the outer loop
i = 1
# Outer loop to iterate through numbers 1 to 10
while i <= 10:
    # Initialize the starting number for the inner loop
    j = 1
    # Inner loop to iterate through numbers 1 to 10
    while j <= 10:
        # Calculate and print the product
        product = i * j
        print(f"{i} x {j} = {product}")
        # Increment the inner loop counter
        j += 1
    # Move to the next line after each row
    print()
    # Increment the outer loop counter
    i += 1

# nested while loops to print a multiplication table from 1 to 10.

'''
Explanation:
Outer Loop (while i <= 10:): This loop controls the first number in the multiplication and runs as long as i is less than or equal to 10.

Inner Loop (while j <= 10:): For each iteration of the outer loop, this inner loop runs, controlling the second number in the multiplication.

Print Statement (print(f"{i} x {j} = {product}")): This statement prints the result of multiplying i by j.

Increment Statements (j += 1 and i += 1): These increment the loop counters, ensuring the loops progress.

Blank Line (print()): This adds a blank line after each row for readability.
'''