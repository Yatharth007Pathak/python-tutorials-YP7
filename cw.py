rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(rows, 0, -1):
    # Inner loop for each column in the current row
    for j in range(1, i + 1):
        # Print the current number in decreasing order
        print(i, end=" ")
    print()  # Move to the next line after each row


# Inverted Right-Angle Triangle with Decreasing Numbers and Left Alignment

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Outer Loop for Rows:
for i in range(rows, 0, -1): initiates a loop that iterates from rows down to 1. Each iteration corresponds to one row in the triangle.

Inner Loop for Columns:
for j in range(1, i + 1): initiates a loop that iterates i times for the current row. This loop prints the number i for each column in the row.

Printing Numbers:
print(i, end=" ") prints the current value of i followed by a space, without moving to a new line. 
This ensures that the number i is printed repeatedly across the row.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''