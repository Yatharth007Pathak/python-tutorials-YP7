'''
return:
Purpose: Used to exit a function and optionally pass back a value to the caller.
Behavior: When a return statement is executed, the function terminates,
and the value specified in the return statement is sent back to the caller. This value can then be used or stored.
'''
def add(x, y):
    return x + y
result = add(5, 3)  # result is now 8


'''
print:
Purpose: Used to output information to the console or terminal for display purposes.
Behavior: The print statement does not affect the function's return value. It simply outputs the specified value(s) to the screen.
'''
def addi(x, y):
    print(x + y)
addi(5, 3)  # This will print 8 to the console


'''
Key Differences:
return sends a value back to the caller and ends the function, 
while print displays information on the console but does not alter the function's return value.
A function with a return statement can provide a result that can be used elsewhere in the program, 
whereas print is typically used for debugging or user notifications.
'''
def addition(x, y):
    result = x + y
    print(f"The result is: {result}")
    return result
sum_result = addition(5, 3)  # Prints "The result is: 8" and sum_result is 8