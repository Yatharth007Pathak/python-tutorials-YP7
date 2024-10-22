n = int(input("Enter n: "))

for i in range(n):  
    for j in range(1, n+1):
        print(j, end = " ")
    print()


# Python program that prints a square pattern of numbers (1,2,3,4,.....), consisting of n rows and columns

'''
Here's a breakdown of the code:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines how many rows of numbers will be printed.

Outer Loop (Row Iteration):
for i in range(n): initiates a loop that iterates n times. Each iteration corresponds to a single row of numbers.

Inner Loop (Column Printing):
for j in range(1, n+1): creates another loop inside the outer loop. 
This loop iterates from 1 through n (inclusive), printing numbers in each row.

Printing Numbers:
print(j, end = " ") prints the current value of j followed by a space, without moving to a new line. 
This ensures that numbers in the same row are printed on the same line, separated by spaces.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.

In summary, this code prints a grid of numbers where each row contains numbers from 1 to n, and there are n such rows.
'''