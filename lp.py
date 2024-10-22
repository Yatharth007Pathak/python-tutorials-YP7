# random module

import random

# Generate a random float in [0.0, 1.0)
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
