# Mutual recursion occurs when two or more functions call each other in a cycle. Without proper termination conditions, this can lead to a stack overflow.


def func_a():
    return func_b()

def func_b():
    return func_a()

# This will cause a stack overflow (RecursionError)
func_a()