n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print('  ' * (n - i) + '* ' * (2 * i - 1))

# Print inverted pyramid pattern of asterisks

'''
Here's a breakdown of the code that prints an inverted pyramid pattern:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines the height of the pyramid.

Loop for Rows:
for i in range(n, 0, -1): initiates a loop that starts from n and decrements down to 1 (inclusive). 
Each iteration corresponds to a row in the inverted pyramid.

Spaces for Centering:
' ' * (n - i) generates leading spaces for each row. The number of spaces increases as i decreases, ensuring the pattern is centered.

Stars Printing:
'* ' * (2 * i - 1) generates the stars for each row. The number of stars decreases with each row, following the pattern (2 * i - 1).

In summary, this code prints an inverted pyramid pattern. 
The number of stars decreases with each row, and the number of leading spaces increases to maintain the centered appearance of the pattern. 
The height of the pyramid is n rows, with the widest row at the top and narrowing as you move downward.
'''