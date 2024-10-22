a = 5  # 0101 in binary
b = 3  # 0011 in binary

# Bitwise AND
and_result = a & b  # 0001 in binary, 1 in decimal

# Bitwise OR
or_result = a | b  # 0111 in binary, 7 in decimal

# Bitwise XOR
xor_result = a ^ b  # 0110 in binary, 6 in decimal

# Bitwise NOT
not_result = ~a  # 1010 in binary, -6 in decimal (two's complement)

# Left Shift
left_shift_result = a << 1  # 1010 in binary, 10 in decimal

# Right Shift
right_shift_result = a >> 1  # 0010 in binary, 2 in decimal

print(f"AND: {and_result}")
print(f"OR: {or_result}")
print(f"XOR: {xor_result}")
print(f"NOT: {not_result}")
print(f"Left Shift: {left_shift_result}")
print(f"Right Shift: {right_shift_result}")


'''
Bitwise operators are used to perform operations on binary representations of numbers. 
They operate at the bit level and are often used in low-level programming, cryptography, graphics, and situations where performance is crucial. 
Here are the various bitwise operators available in most programming languages:

1. Bitwise AND (&)
Operation: Compares each bit of two numbers. The resulting bit is 1 if both corresponding bits are 1, otherwise, it's 0.
Example:
5 & 3 (in binary 0101 & 0011) results in 0001, which is 1 in decimal.

2. Bitwise OR (|)
Operation: Compares each bit of two numbers. The resulting bit is 1 if at least one of the corresponding bits is 1.
Example:
5 | 3 (in binary 0101 | 0011) results in 0111, which is 7 in decimal.

3. Bitwise XOR (^)
Operation: Compares each bit of two numbers. The resulting bit is 1 if the corresponding bits are different, otherwise, it's 0.
Example:
5 ^ 3 (in binary 0101 ^ 0011) results in 0110, which is 6 in decimal.

4. Bitwise NOT (~)
Operation: Inverts each bit of a number. 0 becomes 1 and 1 becomes 0.
Example:
~5 (in binary ~0101) results in 1010, which is -6 in decimal (due to two's complement representation for negative numbers).

5. Left Shift (<<)
Operation: Shifts the bits of a number to the left by a specified number of positions. Each left shift effectively multiplies the number by 2.
Example:
5 << 1 (in binary 0101 << 1) results in 1010, which is 10 in decimal.

6. Right Shift (>>)
Operation: Shifts the bits of a number to the right by a specified number of positions. Each right shift effectively divides the number by 2.
Example:
5 >> 1 (in binary 0101 >> 1) results in 0010, which is 2 in decimal.
'''

"""
Two's Complement Representation
In two's complement, positive and negative integers are represented in a way that allows for straightforward binary arithmetic. 
The most significant bit (MSB) is used as the sign bit:
If the MSB is 0, the number is positive.
If the MSB is 1, the number is negative.

The bitwise NOT operation (~) flips all bits in the binary representation of a number. This means that every 0 becomes 1 and every 1 becomes 0.

Example: Bitwise NOT of 5
Binary Representation of 5: Decimal 5 is represented as 0101 in binary.

Bitwise NOT Operation:
Invert all bits: 0101 becomes 1010 for a 4-bit representation. However, Python typically works with 32-bit integers 
(or more depending on the system), so let's use an 8-bit representation to make it easier to see the effect:
5 in 8-bit binary: 00000101
Bitwise NOT of 5: 11111010

Two's Complement of 11111010:
The result 11111010 is in two's complement form for a negative number.
To find the decimal equivalent, calculate the two's complement:
Invert the bits: 000000101
Add 1: 00000101 + 1 = 00000110
The decimal equivalent of 00000110 is 6.
Therefore, 11110011 represents -6 in two's complement.

Summary
The bitwise NOT operation on 5 (binary 00000101) results in -6
because the inverted bits (11111010) are interpreted as a negative number in two's complement representation.
"""