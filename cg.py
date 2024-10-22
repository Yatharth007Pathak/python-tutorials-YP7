n = int(input("Enter n: "))

for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * (2 * i - 1))

# Print pyramid pattern of asterisks

'''
Here's a breakdown of this code:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines the height of the pyramid pattern.

Loop for Rows:
for i in range(1, n + 1): initiates a loop that iterates from 1 to n (inclusive). Each iteration corresponds to a row in the pyramid.

Spaces for Centering:
' ' * (n - i) generates leading spaces for each row. The number of spaces decreases as i increases, ensuring the pyramid is centered. 
For each row i, the number of spaces is (n - i), which decreases with each row.

Stars Printing:
'* ' * (2 * i - 1) generates the stars for each row. The number of stars increases with each row, following the pattern (2 * i - 1). 
This ensures the pyramid shape with an odd number of stars centered on each row.

In summary, this code prints a centered pyramid pattern of stars. 
The height of the pyramid is n rows, with the number of stars increasing as you move down, 
while the number of leading spaces decreases to center the stars.
'''