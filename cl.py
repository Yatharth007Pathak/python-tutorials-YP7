rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
num = 1   # Starting number

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for each column in the current row
    for j in range(1, i + 1):
        # Print the current number
        print(num, end=" ")
        num += 1  # Increment the number
    print()  # Move to the next line after each row


# Right Angle Triangle with Numbers Increasing Overall

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines how many rows will be printed in the triangle.

Initialize Starting Number:
num = 1 initializes a variable num to keep track of the current number to be printed. 
It starts at 1 and increments with each number printed.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 to rows (inclusive). 
Each iteration corresponds to one row in the triangle.

Inner Loop for Numbers:
for j in range(1, i + 1): initiates a loop that iterates from 1 to i (inclusive). This loop prints numbers for the current row.

Printing Numbers:
print(num, end=" ") prints the current value of num followed by a space, without moving to a new line. 
This ensures that numbers in the same row are printed on the same line, separated by spaces.
num += 1 increments the value of num by 1 after each print, ensuring the numbers continue sequentially across rows.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''