def describe_number(x):
    match x:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2 | 3 | 4:
            return "Small number"
        case _:
            return "Some other number"

print(describe_number(0))  # Output: Zero
print(describe_number(3))  # Output: Small number
print(describe_number(10)) # Output: Some other number


'''
The match-case statement in Python, is a control flow statement similar to the switch or case statements found in other languages. 
It allows you to match values against patterns, making it easier to write complex conditional logic in a clear and concise way. 
This feature is particularly useful for pattern matching
'''