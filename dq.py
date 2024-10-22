size = int(input("Enter the size of square: "))  # Size of the square
num = 1   # Starting number

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print consecutive numbers
        print(num, end=" ")
        num += 1
    print()  # Move to the next line after each row

# Square Pattern with Consecutive Numbers

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square, which determines both the number of rows and columns.

Variable Initialization:
num = 1 initializes the starting number for printing. This variable will increment with each printed number.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column within the current row. This loop also runs size times for each row.

Print Consecutive Numbers:
print(num, end=" ") prints the current value of num followed by a space.
num += 1 increments the number for the next column.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''