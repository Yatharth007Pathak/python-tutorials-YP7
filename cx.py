rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
num = 1   # Starting number

# Outer loop for each row
for i in range(rows, 0, -1):
    # Print numbers in increasing order
    for j in range(i):
        print(num, end=" ")
    num += 1  # Increment the number
    print()  # Move to the next line after each row


# Inverted Right-Angle Triangle with Decreasing Rows but Constant Start Number

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Initialize Starting Number:
num = 1 initializes a variable num to keep track of the current number to be printed. It starts at 1 and increments with each row.

Outer Loop for Rows:
for i in range(rows, 0, -1): initiates a loop that iterates from rows down to 1. Each iteration corresponds to one row in the triangle.

Inner Loop for Numbers:
for j in range(i): initiates a loop that iterates i times for the current row. This loop prints the number num for each column in the row.

Printing Numbers:
print(num, end=" ") prints the current value of num followed by a space, without moving to a new line. 
This ensures that the number num is printed repeatedly across the row.

Increment the Number:
num += 1 increments the value of num by 1 after completing each row, so the next row will use the next number.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''