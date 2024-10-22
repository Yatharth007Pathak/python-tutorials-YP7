n = int(input("Enter n: "))

for i in range(1, n + 1):
    print('* ' * i)

# Print right-angle triangle pattern of asterisks

'''
Here's a breakdown of the code:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines the number of rows in the pattern.

Loop for Rows:
for i in range(1, n + 1): initiates a loop that iterates from 1 to n (inclusive). Each iteration corresponds to a row in the pattern.

Printing Stars:
print('* ' * i) prints a string composed of '* ' repeated i times. 
The multiplication '* ' * i creates a string where the star symbol followed by a space is repeated i times. 
For each row, the number of stars increases by one.

n summary, this code prints a right-angled triangle pattern of stars. 
The number of stars increases with each subsequent row, starting from 1 star in the first row up to n stars in the last row.
'''