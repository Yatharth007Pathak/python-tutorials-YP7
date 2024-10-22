# Accessing items in a Python set 

fruits = {"apple", "banana", "cherry", "date", "kiwi", "papapya"}

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# If we need both the index and the value during iteration, you can use the enumerate() function
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
# 3 date
# 4 kiwi
# 5 papaya