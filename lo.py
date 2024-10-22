"""
The random module in Python provides a suite of functions for generating random numbers and performing random operations. 
It includes functions for generating random integers, floating-point numbers, and performing various random choices and shuffling operations.
Here's a summary of some commonly used functions in the random module:

random.random(): Returns a random floating-point number in the range [0.0, 1.0).
random.uniform(a, b): Returns a random floating-point number between a and b (inclusive).
random.randint(a, b): Returns a random integer between a and b (inclusive).
random.choice(sequence): Returns a randomly selected element from a non-empty sequence (such as a list or tuple).
random.choices(population, weights=None, k=1): Returns a list of k elements chosen from population with optional weights.
random.sample(population, k): Returns a list of k unique elements from population.
random.shuffle(sequence): Shuffles the elements of sequence in place.
random.seed(a=None): Initializes the random number generator with a seed value for reproducibility.
"""

import random

# Generate a random float in the range [0.0, 1.0)
print(f"Random float between 0.0 and 1.0: {random.random()}")

# Generate a random float between 1.5 and 5.5
print(f"Random float between 1.5 and 5.5: {random.uniform(1.5, 5.5)}")

# Generate a random integer between 1 and 10 (inclusive)
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")

# Choose a random element from a list
my_list = ['apple', 'banana', 'cherry']
print(f"Random choice from list: {random.choice(my_list)}")

# Choose 2 random elements from a list with possible repetitions
print(f"Two random choices from list: {random.choices(my_list, k=2)}")

# Choose 2 unique random elements from a list
print(f"Two unique choices from list: {random.sample(my_list, k=2)}")

# Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Seed the random number generator for reproducibility
random.seed(42)
print(f"Random float with seed 42: {random.random()}")

# Re-seeding to show reproducibility
random.seed(42)
print(f"Random float with seed 42 (again): {random.random()}")

# Generate a random float with a different seed
random.seed(7)
print(f"Random float with seed 7: {random.random()}")
