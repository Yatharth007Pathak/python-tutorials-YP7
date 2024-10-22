# Size of the square
n = int(input("Enter the size of square: "))  # Size of the square

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(chr(65 + (i * n + j) % 26), end=" ")  # Letters (A-Z)
        else:
            print((i * n + j) % 10, end=" ")  # Numbers (0-9)
    print()

# Basic Alphanumeric Square Pattern

'''
Code Explanation

Input Collection:
n = int(input("Enter the size of square: ")) asks the user for the size of the square grid. The grid will have n rows and n columns.

Outer Loop for Rows:
for i in range(n): iterates through each row, from 0 to n-1.

Inner Loop for Columns:
for j in range(n): iterates through each column within the current row.

Checkerboard Pattern Logic:
if (i + j) % 2 == 0: checks if the sum of the row and column indices is even.
If true, print(chr(65 + (i * n + j) % 26), end=" ") prints a letter.
chr(65 + (i * n + j) % 26) calculates the letter by using the ASCII value of 'A' (65) 
and adding the current position index (i * n + j) modulo 26 (since there are 26 letters in the alphabet).
else: for odd index sums, it prints a number.
print((i * n + j) % 10, end=" ") calculates a number using the current position index modulo 10, ensuring the numbers cycle from 0 to 9.

New Line for Each Row:
print() moves the output to a new line after each row is printed.
'''