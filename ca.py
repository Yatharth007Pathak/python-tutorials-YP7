"""
Pattern printing in Python refers to generating and displaying various patterns or shapes using characters 
(usually asterisks *, hash symbols #, or other symbols) arranged in a specific format. 
It's a common exercise for beginners to practice loops and understand how to manipulate the flow of control in programs.

How Patterns Work
Loops: Patterns are generally created using nested loops. An outer loop often controls the rows, 
while inner loops manage the characters printed on each row.
String Multiplication: You can use string multiplication ('*' * n) to repeat a character n times.
Spacing: For patterns like pyramids and diamonds, spaces are added before the stars to align the pattern correctly.
"""

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    print('* ' * m)

# Python program that prints a rectangular pattern of asterisks (*), consisting of n rows and m columns

'''
Explanation:

User Input:
The program first prompts the user to input the number of rows (n).
Then it prompts the user to input the number of columns (m).

For Loop:
The outer loop for i in range(n): iterates n times, once for each row.
Inside the loop, the statement print('* ' * m) prints a row of m asterisks. 
The space after * ensures that there is a space between each asterisk for better readability.

Output:
The result is a rectangular pattern of asterisks with n rows and m columns.
'''