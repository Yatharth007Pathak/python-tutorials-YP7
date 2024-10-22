size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print numbers incrementing by column
        print(j + 1, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Incrementing Numbers

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square. 
This determines both the number of rows and columns in the square grid.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. It runs size times.

Inner Loop for Columns:
for j in range(size): iterates through each column of the current row. It also runs size times for each row.

Print Numbers:
print(j + 1, end=" ") prints numbers starting from 1 up to size, with a space after each number. j + 1 ensures that the numbers start from 1 rather than 0.

Line Break:
print() after the inner loop moves the cursor to the next line after finishing the current row.
'''