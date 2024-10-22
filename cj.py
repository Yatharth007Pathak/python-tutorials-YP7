n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()

# Print right-angle triangle pattern of numbers(1,2,3,4,...)

'''
Here's a breakdown of the code that prints a pattern of incremental numbers:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines the number of rows in the pattern.

Outer Loop for Rows:
for i in range(1, n + 1): initiates a loop that iterates from 1 to n (inclusive). Each iteration corresponds to a row in the pattern.

Inner Loop for Numbers:
for j in range(1, i + 1): creates another loop inside the outer loop. This loop iterates from 1 to i. 
It prints numbers in each row.

Printing Numbers:
print(j, end = " ") prints the current value of j followed by a space, without moving to a new line. 
The end=" " parameter prevents moving to a new line after printing j, so the numbers are printed on the same line separated by spaces.

Line Break:

print() after the inner loop finishes printing all numbers for the current row, 
this print() statement moves the cursor to the next line, preparing for the next row of numbers.

In summary, this code prints a pattern of increasing numbers. Each row starts from 1 and ends at i - 1, where i is the current row number. 
The pattern forms a triangle of numbers where the number of elements in each row increases from 0 up to n - 1.
'''