# Infinite while Loop with a Break Condition that Never Executes: We can create an infinite loop by placing a break condition that is impossible to reach.

def unreachable_break_condition():
    i = 0
    while True:
        print(f"Loop iteration {i}")
        i += 1
        if i < 0:  # This condition is never true
            break

unreachable_break_condition()

'''
Explanation: The loop checks if i is less than 0 to break, 
but since i starts at 0 and keeps increasing, the condition i < 0 will never be met, making the loop infinite.
'''