rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
start_char = 'F'  # Starting character

# Convert starting character to ASCII value
char = ord(start_char)

# Outer loop for each row
for i in range(rows):
    # Print characters starting from the current char and increment
    for j in range(i + 1):
        print(chr(char), end=" ")
        char += 1  # Move to the next character
    print()  # Move to the next line after each row


# Right-Angle Triangle with Characters Starting from a Custom Letter

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter the number of rows for the triangle.

Starting Character:
start_char = 'F' defines the starting character for the pattern.

Convert Starting Character to ASCII Value:
char = ord(start_char) converts the starting character ('F') to its corresponding ASCII value. 
The ord() function returns the ASCII value of 'F', which is 70.

Outer Loop for Rows:
for i in range(rows): iterates from 0 up to rows - 1. Each iteration represents a row in the pattern.

Print Characters and Increment:
for j in range(i + 1): iterates for the number of characters to print in the current row, which is i + 1.
print(chr(char), end=" ") prints the character corresponding to the current ASCII value of char. 
The chr() function converts the ASCII value back to its character.
char += 1 increments the ASCII value by 1 after each character is printed, so the next character in the sequence is used for the following print.

Line Break:
print() after the inner loop prints a newline character to move to the next line.
'''