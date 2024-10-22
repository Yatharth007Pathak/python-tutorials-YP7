n = int(input("Enter n: "))

# Print upper half of the diamond
for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * (2 * i - 1))

# Print lower half of the diamond
for i in range(n - 1, 0, -1):
    print('  ' * (n - i) + '* ' * (2 * i - 1))


# Print Diamond Pattern of asterisks

'''
Here's a breakdown of the code that prints a diamond pattern:

Input Collection:
n = int(input("Enter n: ")) prompts the user to enter an integer value for n. This value determines the height of the upper half of the diamond.

Upper Half of the Diamond:
for i in range(1, n + 1): loops from 1 to n (inclusive) to print the upper half of the diamond.
' ' * (n - i) generates the leading spaces for centering the stars. The number of spaces decreases as i increases.
'* ' * (2 * i - 1) generates the stars for each row. The number of stars increases with each row, creating the upper part of the diamond.

Lower Half of the Diamond:
for i in range(n - 1, 0, -1): loops from n - 1 down to 1 (inclusive) to print the lower half of the diamond.
' ' * (n - i) generates the leading spaces for centering the stars, similar to the upper half but in reverse order.
'* ' * (2 * i - 1) generates the stars for each row, decreasing as i decreases, forming the lower part of the diamond.

In summary, this code prints a diamond pattern where the upper half is created by increasing the number of stars and decreasing spaces, 
while the lower half is created by decreasing the number of stars and increasing spaces. 
The result is a symmetrical diamond shape with a height of 2 * n - 1 rows
'''