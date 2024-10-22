str1 = "6/4"

print("str1")
print(str1)
print(eval(str1))

'''
Here's a breakdown of what each line does:

str1 = "6/4": This line assigns the string "6/4" to the variable str1. The string represents a mathematical expression (division of 6 by 4).

print("str1"): This line prints the string "str1" as it is, without evaluating its content. The output will literally be the text str1.

print(str1): This line prints the value stored in the variable str1, which is the string "6/4". The output will be 6/4.

print(eval(str1)): This line evaluates the expression contained in the string str1 using the eval() function. 
The eval() function interprets the string as a Python expression and executes it. 
In this case, it performs the division 6/4, which results in 1.5, and then prints this result.

Summary of Outputs:

The first print outputs: str1
The second print outputs: 6/4
The third print outputs: 1.5
'''