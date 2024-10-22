"""
Pip is a package manager for python. It allows us to install and manage additional libraries and packages 
that aren't included with python by default.
With Pip, we can easily add tools and libraries to our project. think of Pip as an app store for python packages.
We can install packages using Pip direcly from our terminal or command prompt.

To install Python libraries, we can use pip, which is the package installer for Python. Here's how we can do it:

Open a terminal in VS Code and type:

1. Using the Command Line/Terminal:
Basic Installation: pip install library_name   (Replace library_name with the name of the library we want to install)
Example: To install the numpy library, we would run: pip install numpy
Installing Specific Versions: If we need a specific version of a library, we can specify it like this: pip install library_name==version_number
Example: pip install numpy==1.21.0
Upgrading a Library: To upgrade an already installed library to the latest version: pip install --upgrade library_name
Installing Multiple Libraries: We can install multiple libraries at once by listing them separated by spaces: pip install lib1 lib2 liby3
Uninstalling a library. To remove a library, we can use: pip uninstall library_name

2. Using requirements.txt:
If we have a list of libraries and versions that we want to install, we can create a requirements.txt file and install them all at once.
Create a requirements.txt File:
numpy==1.21.0
pandas==1.3.1
matplotlib==3.4.2
Install Libraries from requirements.txt:
pip install -r requirements.txt

Check Installed Libraries:
To see a list of all installed libraries: pip list
"""

# Install NumPy
'''
We can install NumPy using pip. Open a terminal in VS Code and type:
pip install numpy
'''

# Verify the Installation: After installation, try running the following simple script in VS Code:
import numpy as np

# Check if NumPy is working
print(np.__version__)               # If it prints the version of NumPy, then the installation is successful.
