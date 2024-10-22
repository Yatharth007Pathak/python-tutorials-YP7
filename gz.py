'''
Infinite Loop with No Iteration Overhead
In some cases, infinite loops are created without any overhead, 
such as incrementing a counter, and these loops are especially dangerous because they do not give any indication of progress.
'''


def infinite_no_iteration():
    while True:
        pass  # Do nothing, just loop infinitely

infinite_no_iteration()

# Explanation: This loop does nothing inside but will run forever. It's an infinite loop with no overhead.