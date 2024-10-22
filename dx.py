size = int(input("Enter the size of square: "))  # Size of the square
char = str(input("Enter the character: "))  # Alphabet to fill the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print the same alphabet in all cells
        print(char, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Same Alphabet in All Cells

'''
Code Explanation

Input Collection:
size = int(input("Enter the size of square: ")) takes the size of the square grid from the user.
char = str(input("Enter the character: ")) takes the character to fill the square from the user.

Outer Loop for Rows:
for i in range(size): iterates over each row of the grid.

Inner Loop for Columns:
for j in range(size): iterates over each column within the current row.

Print Character:
print(char, end=" ") prints the same character for each cell in the current row.
end=" " ensures that characters are printed with a space in between, but no newline after each character.

Line Break:
print() moves to the next line after completing each row.
'''