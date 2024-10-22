# Input the number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
# Outer loop for each row
for i in range(rows):
    # Inner loop for each column
    for j in range(columns):
        # Print an asterisk followed by a space
        print('*', end=' ')
    # Move to the next line after each row
    print()

# Python program that prints a rectangular pattern of asterisks (*), consisting of n rows and m columns using nested for loop

'''
code brakdown:

rows = int(input("Enter the number of rows: "))
Prompts the user to input the number of rows for the pattern.
Converts the input from a string to an integer and assigns it to the variable rows.

columns = int(input("Enter the number of columns: "))
Prompts the user to input the number of columns for the pattern.
Converts the input from a string to an integer and assigns it to the variable columns.

Outer Loop for Rows:
for i in range(rows):
Iterates from 0 to rows-1.
Each iteration corresponds to one row in the output.

Inner Loop for Columns:
for j in range(columns):
Iterates from 0 to columns-1.
Each iteration corresponds to one column in the current row.

print('*', end=' ')
Prints an asterisk (*) followed by a space.
The end=' ' argument ensures that the print statement does not move to a new line after printing the asterisk but stays on the same line.

print()
After the inner loop completes (i.e., after printing all columns for a row), 
this print() statement moves the cursor to the next line, starting a new row.
'''