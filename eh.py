# list Comprehension

numbers = [10, 20, 30, 40, 50]
newlist = []
new_list = []

for i in numbers:
    if i > 25:
        newlist.append(i)

print(newlist)

new_list = [i for i in numbers if i > 25]
print(new_list)

'''
The code we provided does two things:
It filters the list numbers to include only elements greater than 25 using a for loop and if statement, and stores the result in newlist.
It achieves the same filtering but in a more concise way using list comprehension and stores the result in new_list.
'''

'''
Code breakdown for first part:-
The for loop iterates over each element in numbers.
The if condition checks if the element is greater than 25.
If the condition is true, the element is appended to newlist.
Finally, newlist is printed, showing [30, 40, 50]
'''

'''
Code breakdown for second part:-
This line is a list comprehension that does the same filtering in a single line.
It directly creates a new list new_list containing elements greater than 25 from numbers.
The output of new_list is also [30, 40, 50].
'''