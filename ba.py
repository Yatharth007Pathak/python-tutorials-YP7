'''
Conditionals
Conditionals allow us to execute certain pieces of code based on whether a condition is true or false. 
The most common conditional statements are if, elif, and else.
'''

age = 18

if age < 18:
    print("You are under 18.")
elif age == 18:
    print("You are exactly 18.")
else:
    print("You are over 18.")


'''
if checks if the condition is true.
elif (short for "else if") checks another condition if the previous conditions were false.
else runs if none of the previous conditions were true.
'''