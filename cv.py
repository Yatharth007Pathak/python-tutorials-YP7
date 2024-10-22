n = int(input("Enter the number of rows: "))  # Number of rows for the triangle

for i in range(1, n+1):
    # Printing spaces
    print(" " * (n-i), end= "")
    # Printing digits
    for j in range(1, 2 * i):
            print(j, end="")
    print()  # Move to the next line after each row

# Pyramid pattern of numbers, where each row contains a sequence of increasing digits, centered with spaces.

'''
Code Explanation

Input Collection:
n = int(input("Enter the number of rows: ")) prompts the user to enter the number of rows for the pyramid.

Outer Loop for Rows:
for i in range(1, n+1): iterates over each row from 1 to n.

Printing Spaces for Centering:
print(" " * (n-i), end="") prints spaces before the digits to center-align the pyramid.
n-i calculates the number of spaces needed for the current row.

Printing Digits:
for j in range(1, 2 * i): iterates through each number that needs to be printed in the current row.
The range (1, 2 * i) ensures the number of digits increases by 2 in each subsequent row, forming the pyramid shape.
print(j, end="") prints each digit from 1 up to 2 * i - 1 without any space in between.

New Line for Each Row:
print() moves the output to the next line after completing each row.
'''