# Incorrect Base Case: In this example, the base case is incorrectly defined, leading to infinite recursion.


def faulty_base_case(n):
    # Incorrect base case: n will never be 0 or negative
    if n > 0:
        return faulty_base_case(n - 1)
    else:
        # This line is never reached due to incorrect logic
        return "Completed"

# This will cause a stack overflow (RecursionError)
faulty_base_case(10)
