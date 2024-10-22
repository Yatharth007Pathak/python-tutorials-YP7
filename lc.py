# Handling Exceptions in File I/O: We can handle exceptions during file operations using a try-except block.

try:
    with open('text13.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred.")
