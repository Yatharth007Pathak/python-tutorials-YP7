# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

# Print matrix
print("Matrix:")
for row in matrix:
    print(row)


# Input a matrix and print it

'''
Here's a detailed breakdown:

rows = int(input("Enter number of rows: ")):
Prompts the user to enter the number of rows for the matrix.
Converts the user's input from a string to an integer and assigns it to the variable rows.

cols = int(input("Enter number of columns: ")):
Prompts the user to enter the number of columns for the matrix.
Converts the user's input from a string to an integer and assigns it to the variable cols.

matrix = []:
Initializes an empty list named matrix to hold the rows of the matrix.

for i in range(rows)::
Starts a loop that iterates over the range of rows. This loop will create each row of the matrix.

row = []:
Initializes an empty list named row for storing the elements of the current row.

for j in range(cols)::
Starts a nested loop that iterates over the range of cols. This loop will handle the elements in the current row.

element = int(input(f"Enter element for position ({i+1}, {j+1}): ")):
Prompts the user to enter an element for the matrix at the position (i+1, j+1). 
The i+1 and j+1 are used to provide a 1-based index for user clarity.
Converts the input to an integer and assigns it to the variable element.

append is a method used to add elements to a list

row.append(element):
append adds the element (which is an integer entered by the user) to the end of the row list.
This happens within the inner loop, where each element of a row is collected and added to the row list.
row.append(element) adds an individual element to a row.

matrix.append(row):
append adds the completed row list (which contains all the elements of that row) to the end of the matrix list.
This occurs after the inner loop finishes, meaning the row list, now fully populated with elements, is added as a new row to the matrix.
matrix.append(row) adds a complete row to the matrix.

print("Matrix:"):
Prints the header "Matrix:" to indicate that the matrix is about to be printed.

for row in matrix::
Starts a loop that iterates over each row in the matrix.

print(row):
Prints the current row. Each row is displayed as a list of its elements.
'''