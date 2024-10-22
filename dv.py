size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print alphabets decrementing by row
        print(chr(65 + size - i - 1), end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Decrementing Alphabets Each Row

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square grid. 
This determines the number of rows and columns.

Outer Loop for Rows:
for i in range(size): iterates over each row of the grid. This loop will run size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates over each column within the current row. This loop also runs size times for each row.

Print Alphabets Decrementing by Row:
print(chr(65 + size - i - 1), end=" ") prints a character that decreases with each row:
65 is the ASCII value for 'A'.
size - i - 1 calculates the index for the character to print, which decreases as the row index i increases.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''