# Loops allow us to execute a block of code multiple times. The two primary types of loops in Python are for and while.


# For Loop: Used to iterate over a sequence (like a list, tuple, or string).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop: Repeats as long as a condition is true.
count = 0
while count < 3:
    print(count)
    count += 1

'''
Python doesn't have a built-in do-while loop like some other programming languages (e.g., C, C++). 
However, we can simulate a do-while loop using a while loop with a break statement.
The key characteristic of a do-while loop is that it executes the loop body at least once before checking the condition.
'''
# Initialize a variable
number = 0
# Simulate a do-while loop
while True:
    # Code block that should run at least once
    print("Number is:", number)
    number += 1
    # Condition to break the loop
    if number >= 5:
        break
