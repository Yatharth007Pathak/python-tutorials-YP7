size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print alphabets incrementing by row
        print(chr(65 + i), end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Incrementing Alphabets Each Row

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square grid, 
which will determine both the number of rows and columns.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column within the current row. This loop also runs size times for each row.

Print Alphabets Incrementing by Row:
print(chr(65 + i), end=" ") prints characters starting from 'A' (ASCII value 65) and increments based on the row index i.
chr(65 + i) converts the ASCII value to a character, where 65 is the ASCII value for 'A' and i is the row index.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''