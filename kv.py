'''
"r+": Read and Write
Opens the file for both reading and writing. The file pointer is placed at the beginning of the file.
If the file does not exist, an error occurs.
'''

with open("text6.txt", "r+") as file:
    content = file.read()
    print("Original content:", content)
    file.write("\nAdding new content.")
