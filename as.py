'''
Operators in Python are special symbols that perform operations on variables and values. 
Python supports several types of operators, each serving a different purpose
'''


"""
Arithmetic Operators: Used for basic mathematical operations.
+: Addition (5 + 3 equals 8)
-: Subtraction (5 - 3 equals 2)
*: Multiplication (5 * 3 equals 15)
/: Division (5 / 3 equals 1.6667)
%: Modulus (remainder of division, 5 % 3 equals 2)
**: Exponentiation (5 ** 3 equals 125)
//: Floor division (division that rounds down, 5 // 3 equals 1)
"""
a = 10
b = 3
addition = a + b          # Addition
subtraction = a - b       # Subtraction
multiplication = a * b    # Multiplication
division = a / b          # Division
modulus = a % b           # Modulus
exponentiation = a ** b   # Exponentiation
floor_division = a // b   # Floor Division
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)


"""
Comparison Operators: Used to compare two values.
==: Equal to (5 == 3 is False)
!=: Not equal to (5 != 3 is True)
>: Greater than (5 > 3 is True)
<: Less than (5 < 3 is False)
>=: Greater than or equal to (5 >= 3 is True)
<=: Less than or equal to (5 <= 3 is False)
"""
x = 10
y = 20
equal = (x == y)          # Equal to
not_equal = (x != y)      # Not equal to
greater_than = (x > y)   # Greater than
less_than = (x < y)      # Less than
greater_equal = (x >= y) # Greater than or equal to
less_equal = (x <= y)    # Less than or equal to
print("Equal:", equal)
print("Not Equal:", not_equal)
print("Greater Than:", greater_than)
print("Less Than:", less_than)
print("Greater or Equal:", greater_equal)
print("Less or Equal:", less_equal)


"""
Logical Operators: Used to combine conditional statements.
and: Returns True if both statements are true (True and False is False)
or: Returns True if one of the statements is true (True or False is True)
not: Reverses the result (not True is False)
"""
c = True
d = False
logical_and = c and d     # Logical AND
logical_or = c or d       # Logical OR
logical_not = not c       # Logical NOT
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)


"""
Assignment Operators: Used to assign values to variables.
=: Assigns a value (x = 5)
+=: Adds and assigns (x += 3 is equivalent to x = x + 3)
-=: Subtracts and assigns (x -= 3 is equivalent to x = x - 3)
*=: Multiplies and assigns (x *= 3 is equivalent to x = x * 3)
/=: Divides and assigns (x /= 3 is equivalent to x = x / 3)
%=: Modulus and assigns (x %= 3 is equivalent to x = x % 3)
**=: Exponentiates and assigns (x **= 3 is equivalent to x = x ** 3)
//=: Floor divides and assigns (x //= 3 is equivalent to x = x // 3)
"""
e = 5
e += 3    # e = e + 3
e -= 2    # e = e - 2
e *= 4    # e = e * 4
e /= 2    # e = e / 2
e %= 3    # e = e % 3
e **= 2   # e = e ** 2
e //= 2   # e = e // 2
print("Updated e:", e)


"""
Bitwise Operators: Used to perform bit-level operations.
&: AND (5 & 3 equals 1)
|: OR (5 | 3 equals 7)
^: XOR (5 ^ 3 equals 6)
~: NOT (~5 equals -6)
<<: Left shift (5 << 1 equals 10)
>>: Right shift (5 >> 1 equals 2)
"""
p = 12  # Binary: 1100
q = 5   # Binary: 0101
bitwise_and = p & q     # Bitwise AND
bitwise_or = p | q      # Bitwise OR
bitwise_xor = p ^ q     # Bitwise XOR
bitwise_not = ~p        # Bitwise NOT
bitwise_left_shift = p << 2  # Bitwise Left Shift
bitwise_right_shift = p >> 2 # Bitwise Right Shift
print("Bitwise AND:", bitwise_and)                        # p (1100) AND q (0101) results in 0100, which is 4 in decimal.
print("Bitwise OR:", bitwise_or)                          # p (1100) OR q (0101) results in 1101, which is 13 in decimal
print("Bitwise XOR:", bitwise_xor)                        # p (1100) XOR q (0101) results in 1001, which is 9 in decimal.
print("Bitwise NOT:", bitwise_not)                        # NOT p (1100) inverts all bits, resulting in -1101, which is -13 in decimal. The negative result is due to two's complement representation of signed integers in binary.
print("Bitwise Left Shift:", bitwise_left_shift)          # Left shifting p (1100) by 2 positions results in 110000, which is 48 in decimal.
print("Bitwise Right Shift:", bitwise_right_shift)        # Right shifting p (1100) by 2 positions results in 0011, which is 3 in decimal.


"""
Membership Operators: Used to test if a sequence contains an item.
in: Returns True if a value is found in a sequence ("a" in "apple" is True)
not in: Returns True if a value is not found in a sequence ("b" not in "apple" is True)
"""
fruits = ["apple", "banana", "cherry"]
in_list = "banana" in fruits   # Checks if 'banana' is in the list
not_in_list = "grape" not in fruits  # Checks if 'grape' is not in the list
print("'banana' in list:", in_list)    #  This evaluates to True because "banana" is indeed an element in the fruits list.
print("'grape' not in list:", not_in_list)    # This evaluates to True because "grape" is not present in the fruits list.


"""
Identity Operators: Used to compare the memory locations of two objects.
is: Returns True if both variables point to the same object (x is y)
is not: Returns True if both variables point to different objects (x is not y)
"""
i = [1, 2, 3]
j = i
k = [1, 2, 3]
same_object = (i is j)      # Checks if i and j are the same object
different_object = (i is not k)  # Checks if i and k are different objects
print("i is j:", same_object)    # This evaluates to True because j is assigned to i, making them references to the same list object in memory.
print("i is not k:", different_object)    # True because even though i and k have the same contents, they are different objects in memory. k is a new list with the same elements, but it's not the same object as i