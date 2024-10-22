'''
"t": Text Mode (Default)
The default mode if you don't specify a mode.
Text mode is used for reading and writing strings, with automatic encoding and decoding of text.
'''

# No need to specify "t" explicitly as it is the default mode
with open("text10.txt", "rt") as file:
    content = file.read()
    print(content)
