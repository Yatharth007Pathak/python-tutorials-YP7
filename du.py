size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print decrementing alphabets
        print(chr(65 + size - j - 1), end=" ")
    print()  # Move to the next line after each row

#  Square Pattern with Decrementing Alphabets

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) collects the size of the square grid from the user. 
This determines the number of rows and columns.

Outer Loop for Rows:
for i in range(size): iterates through each row of the grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column in the current row. This loop also runs size times for each row.

Print Decrementing Alphabets:
print(chr(65 + size - j - 1), end=" ") prints characters starting from the end of the alphabet sequence for the current row.
65 is the ASCII value for 'A'.
size - j - 1 calculates the position in the alphabet sequence, 
decrementing with each column to produce characters in decreasing order for each row.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''