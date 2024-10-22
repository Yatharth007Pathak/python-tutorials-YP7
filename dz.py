# Size of the square
n = int(input("Enter hte number of rows: "))

# Initialize counters for letters and numbers
letter_counter = 0
number_counter = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(chr(65 + (letter_counter % 26)), end=" ")  # Letters (A-Z)
            letter_counter += 1
        else:
            print(number_counter % 10, end=" ")  # Numbers (0-9)
            number_counter += 1
    print()

# Square Pattern with Alternating Rows

'''
Code Explanation

Input Collection:
n = int(input("Enter the number of rows: ")) asks the user for the size of the square grid, which will have n rows and n columns.

Initialize Counters:
letter_counter = 0 and number_counter = 0 are used to keep track of which letter or number to print next.

Outer Loop for Rows:
for i in range(n): iterates through each row, from 0 to n-1.

Inner Loop for Columns:
for j in range(n): iterates through each column within the current row.

Alternating Rows Logic:
if i % 2 == 0: checks if the row index i is even.
If true, print(chr(65 + (letter_counter % 26)), end=" ") prints a letter.
chr(65 + (letter_counter % 26)) calculates the letter by using the ASCII value of 'A' (65) and adding the current letter_counter modulo 26, ensuring that the letters cycle from A to Z.
letter_counter += 1 increments the letter counter after each letter is printed.
else: for odd-indexed rows, it prints a number.
print(number_counter % 10, end=" ") calculates a number using the number_counter modulo 10, ensuring that numbers cycle from 0 to 9.
number_counter += 1 increments the number counter after each number is printed.

New Line for Each Row:
print() moves the output to a new line after each row is printed.
'''