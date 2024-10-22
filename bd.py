'''
Control statements in programming are constructs that manage the flow of execution of code within a program. 
In Python, control statements include conditional statements, loops, and certain special statements 
like break, continue, and pass that alter the normal sequential execution of code.
'''

'''
 Conditional Statements
These statements allow you to execute certain blocks of code based on conditions.
if Statement: Executes a block of code if a condition is true.
elif Statement: Allows checking multiple expressions for true and executing a block of code as soon as one condition is true.
else Statement: Executes a block of code if all preceding conditions are false.
'''
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

'''
Looping Statements
These statements allow you to repeat a block of code multiple times.
for Loop: Iterates over a sequence (such as a list, tuple, or string).
while Loop: Repeats a block of code as long as a condition is true.
'''
for i in range(5):
    print("i =", i)

count = 0
while count < 5:
    print("count =", count)
    count += 1

'''
Special Control Statements
These are used to control the flow within loops and conditional blocks.
break Statement: Exits the nearest enclosing loop immediately.
continue Statement: Skips the current iteration and moves to the next iteration of the loop.
pass Statement: Does nothing; it can be used as a placeholder for future code.
'''
for j in range(10):
    if j == 5:
        break
    print("j =", j)

for k in range(5):
    if k == 2:
        continue
    print("k =", k)

for m in range(5):
    if m == 2:
        pass  # Placeholder for future code
    else:
        print("m =", m)

'''
else Clause with Loops
Both for and while loops can have an else clause, which executes when the loop is not terminated by a break statement.
'''
for n in range(5):
    if n == 10:
        break
else:
    print("Loop completed without break.")