"""
The os module in Python provides a way of using operating system-dependent functionality like reading or writing to the file system, 
manipulating file paths, and interacting with the environment. It provides a wide range of functions for interacting with the operating system.

Common Functions and Methods

File and Directory Operations
os.name: Returns the name of the operating system dependent module imported ('posix', 'nt', 'os2', 'ce', etc.).
os.getcwd(): Returns the current working directory.
os.chdir(path): Changes the current working directory to the specified path.
os.listdir(path): Returns a list of entries in the directory given by path.
os.mkdir(path): Creates a directory named path.
os.makedirs(path): Recursively creates directories.
os.rmdir(path): Removes (deletes) the directory path.
os.removedirs(path): Removes directories recursively.
os.rename(src, dst): Renames the file or directory from src to dst.
os.remove(path): Removes (deletes) the file path.
os.path.exists(path): Returns True if path exists.
os.path.isfile(path): Returns True if path is a file.
os.path.isdir(path): Returns True if path is a directory.
os.path.join(path, *paths): Joins one or more path components intelligently.
os.path.split(path): Splits the pathname into a pair (head, tail).
os.path.splitext(path): Splits the pathname into a pair (root, ext) where ext is everything after the last dot.

Environment Variables
os.getenv(key, default=None): Returns the value of the environment variable key if it exists, otherwise returns default.
os.environ: A mapping object representing the string environment. Example, os.environ['HOME'] gets the value of the HOME environment variable.

Process Management
os.system(command): Executes the command (a string) in a subshell.
os.execvp(program, arguments): Executes a new program, replacing the current process.
os.exit(status): Exit the process with the given status.
"""


import os

# Get the name of the operating system
print(f"OS name: {os.name}")

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Change the current working directory
# os.chdir('/path/to/directory')

# List files and directories in the current directory
print(f"Directory contents: {os.listdir(current_dir)}")

# Create a new directory
# os.mkdir('new_directory')

# Remove a directory
# os.rmdir('new_directory')

# Rename a file or directory
# os.rename('old_name', 'new_name')

# Check if a path exists and if it is a file or directory
path = 'example.txt'
print(f"Does the path exist? {os.path.exists(path)}")
print(f"Is it a file? {os.path.isfile(path)}")
print(f"Is it a directory? {os.path.isdir(path)}")

# Join and split paths
full_path = os.path.join(current_dir, 'example.txt')
print(f"Full path: {full_path}")
head, tail = os.path.split(full_path)
print(f"Head: {head}, Tail: {tail}")
root, ext = os.path.splitext(full_path)
print(f"Root: {root}, Extension: {ext}")

# Environment variables
home_dir = os.getenv('HOME')
print(f"Home directory: {home_dir}")

# Execute a command
# os.system('echo Hello, World!')

# Exit the process (use cautiously)
# os.exit(0)

'''
File and Directory Operations: Functions for navigating and manipulating the file system.
Environment Variables: Access and modify environment variables.
Process Management: Execute system commands and manage processes.
'''