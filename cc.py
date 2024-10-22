# Input the number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initialize the outer loop counter
i = 0
# Outer loop to iterate through rows
while i < rows:
    # Initialize the inner loop counter
    j = 0
    # Inner loop to iterate through columns
    while j < columns:
        # Print an asterisk followed by a space
        print('*', end=' ')
        # Increment the inner loop counter
        j += 1
    # Move to the next line after each row
    print()
    # Increment the outer loop counter
    i += 1

# Python program that prints a rectangular pattern of asterisks (*), consisting of n rows and m columns using nested while loop

'''
Here's a breakdown of the code you provided:

Input Reading:
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
Purpose: Get the number of rows and columns for the grid from the user.
Function: input() reads user input as a string, and int() converts it to an integer.

Initialize Outer Loop Counter:
i = 0
Purpose: Set up a counter variable i for the outer loop which will iterate through rows.

Outer Loop (Row Iteration):
while i < rows:
Purpose: Control the number of rows. The loop will run as long as i is less than the number of rows.

Initialize Inner Loop Counter:
j = 0
Purpose: Set up a counter variable j for the inner loop which will iterate through columns.

Inner Loop (Column Iteration):
while j < columns:
Purpose: Control the number of columns in each row. The loop will run as long as j is less than the number of columns.

Print Asterisk:
print('*', end=' ')
Purpose: Print an asterisk followed by a space. 
The end=' ' argument prevents the default newline character from being added, so the next asterisk will be printed on the same line.

Increment Inner Loop Counter:
j += 1
Purpose: Increase the counter j by 1 for the inner loop to eventually terminate after printing all columns.

Move to Next Line After Each Row:
print()
Purpose: Print a newline character to move to the next line after completing the current row.

Increment Outer Loop Counter:
i += 1
Purpose: Increase the counter i by 1 for the outer loop to eventually terminate after printing all rows.
'''