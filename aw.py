result = 3 + 2 * (5 ** 2) / (8 - 2)
print(result)
# In this example, 5 ** 2 is evaluated first, followed by the division, multiplication, and finally the addition.

expression =  3 + 2 ** 4 / 2 * 5 - 8 // 2
print(expression)
# In this example, follow the order of operator precedence: Exponentiation, Division, Multiplication, Floor Division, Addition and Subtraction

'''
In Python, operator precedence determines the order in which operations are performed in an expression. 
Here's a summary of the operator precedence in Python, from highest to lowest:

Parentheses (): Alters the precedence order by grouping expressions.
Exponentiation **: Raises a number to the power of another.
Unary Plus and Minus +x, -x: Unary operations (positive or negative sign).
Multiplication *, Division /, Floor Division //, Modulus %: These operators have the same precedence level.
Addition +, Subtraction -: These operators have the same precedence level.
Bitwise Shift Operators <<, >>: Shifts bits left or right.
Bitwise AND &: Performs bitwise AND operation.
Bitwise XOR ^: Performs bitwise XOR operation.
Bitwise OR |: Performs bitwise OR operation.
Comparison Operators: These include ==, !=, >, <, >=, <=, is, is not, in, not in.
Logical NOT not: Negates a boolean expression.
Logical AND and: Returns True if both operands are true.
Logical OR or: Returns True if at least one operand is true.
Conditional Expressions if-else: Returns one of two values based on a condition.
Assignment Operators: These include =, +=, -=, *=, /=, //=, %=, **=, &=, ^=, |=, <<=, >>=.
Expressions Evaluation: Evaluates expressions in the context of the left-to-right and right-to-left rules.
'''