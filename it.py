"""
Consider a string: 'The unexpected always happens "

1. Assign this string to a variable: text.
2. Print the string.
3. Print the length of the string.
4. Check if the phrase 'pp' is present in the string.
5. Print the substring from 0 till 10th index.
6. Replace 'always' with 'never'.
7. Add "no matter what" to the string.
8. Print the final string.
"""

text = "The unexpected always happens "
print(text)
print(len(text))
print(text.find('pp'))
print(text[:11])
print(text.replace('always', 'never'))
text_ = "no matter what"
new_text = text + text_
print(new_text)