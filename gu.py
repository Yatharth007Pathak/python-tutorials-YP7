# Recursive Function with Missing Base Case: Here, a base case might be missing or incorrectly implemented, leading to infinite recursion:

def missing_base_case(n):
    # The function should have a base case to stop the recursion
    # But it's missing here
    return missing_base_case(n - 1)

# This will cause a stack overflow (RecursionError)
missing_base_case(10)