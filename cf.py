n = int(input("Enter n: "))

for i in range(n):
    print('* ' * n)

# Print square pattern of asterisks

'''
Here's a breakdown of this code:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. 
This value determines the number of rows and columns of stars to be printed.

Loop for Rows:
for i in range(n): initiates a loop that iterates n times. Each iteration corresponds to a row in the pattern.

Printing Stars:
print('* ' * n) prints a string composed of '* ' repeated n times. 
The multiplication '* ' * n creates a string where the star symbol followed by a space is repeated n times.
 This results in n stars printed in each row.

In summary, this code prints a square pattern of stars. Each row contains n stars, and there are n such rows, creating a square grid of stars.
'''