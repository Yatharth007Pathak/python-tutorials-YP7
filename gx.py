"""
Infinite for Loop with itertools
You can create an infinite loop using a for loop in combination with the itertools.cycle function, which cycles through an iterable infinitely.
"""

import itertools

def infinite_for_loop():
    for _ in itertools.cycle([1]):
        print("This will print forever!")

infinite_for_loop()

# Explanation: itertools.cycle([1]) will keep cycling through the list [1] infinitely, so the for loop never exits.