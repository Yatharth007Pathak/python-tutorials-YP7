"""
A Python environment is an isolated workspace that allows you to manage dependencies for a specific project independently of other projects.
It ensures that libraries installed in one environment do not interfere with those in another. 
This is particularly useful when working on multiple projects that require different versions of the same library.

Types of Environments: It is a directory that contains a specific Python interpreter and all the libraries installed using pip.
Common tools to create and manage virtual environments include venv and virtualenv.

To create a virtual environment: python -m venv myenv
To activate the virtual environment: 
On Windows: myenv\Scripts\activate
On macOS/Linux: source myenv/bin/activate
To deactivate the virtual environment: deactivate

Conda Environments: If we're using Anaconda, conda environments offer more advanced features, 
such as managing different Python versions and packages.
To create a conda environment: conda create --name myenv
To activate the environment: conda activate myenv
To deactivate the environment: conda deactivate

A Python library is a collection of modules or packages that provide specific functionality, like data manipulation, 
web development, or machine learning. Libraries are installed using pip (or conda for Anaconda users) 
and can be used within a Python project to enhance its capabilities.
Examples of Popular Libraries
NumPy: For numerical computing.
Pandas: For data manipulation and analysis.
Requests: For making HTTP requests.
Matplotlib: For plotting and data visualization.
TensorFlow: For machine learning.

When we create a new environment, it starts with a clean slate, meaning no libraries are installed except for those 
that come with the standard Python distribution. We can then install only the libraries we need for our specific project, 
which helps avoid conflicts and keeps your system organized.
For example, we might have one environment for a web development project that uses Django 
and another environment for a data analysis project that uses Pandas and Matplotlib. 
Each environment can have its own versions of these libraries without affecting each other.
"""