"""
Python has a rich ecosystem of libraries that cater to a wide range of tasks and applications. 
Here are some popular Python libraries categorized by their use:


General-Purpose Libraries
NumPy: Essential for numerical computations, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
Pandas: Excellent for data manipulation and analysis, with powerful data structures like DataFrames, especially useful for manipulating and analyzing structured data (like tables).
Matplotlib: A plotting library used to create static, interactive, and animated visualizations in Python.
Seaborn: Built on top of Matplotlib, it offers a high-level interface for drawing attractive and informative statistical graphics.
SciPy: Used for scientific and technical computing, including modules for optimization, integration, interpolation, eigenvalue problems, etc.
SymPy: A library for symbolic mathematics, useful for algebraic expressions, calculus, and other mathematical computations.

Machine Learning & Data Science
Scikit-learn: A comprehensive library for machine learning, offering simple and efficient tools for data mining and analysis, including classification, regression, clustering, and dimensionality reduction.
TensorFlow: An open-source library for deep learning and machine learning, known for its flexibility and scalability, commonly used for building neural networks.
Keras: A high-level neural networks API, running on top of TensorFlow, designed for quick experimentation.
PyTorch: A deep learning framework that provides a flexible and dynamic approach to neural network implementation.
XGBoost: An optimized gradient boosting library for supervised learning, known for its speed and performance.
Statsmodels: Provides classes and functions for the estimation of many statistical models and tests.

Web Development
Django: A high-level web framework that encourages rapid development and clean, pragmatic design.
Flask: A micro web framework that is lightweight and modular, allowing for easy and quick web application development.
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python-type hints.
Beautiful Soup: A library for web scraping purposes, designed to pull data out of HTML and XML files.
Requests: A simple and elegant HTTP library for making API requests, which simplifies interactions with web services.

Data Visualization
Plotly: A graphing library that makes interactive, publication-quality graphs online.
Bokeh: A library for creating interactive visualizations in the browser using JavaScript.
Altair: A declarative statistical visualization library based on Vega and Vega-Lite visualization grammars.

Natural Language Processing (NLP)
NLTK: The Natural Language Toolkit, a suite of libraries and programs for symbolic and statistical natural language processing.
spaCy: A fast and robust library for NLP, offering features like tokenization, part-of-speech tagging, and named entity recognition.
TextBlob: A simpler NLP library that provides easy-to-use tools for common natural language processing tasks.

Automation & Scripting
Selenium: A tool for automating web applications for testing purposes, but it can also be used to automate any repetitive web tasks.
PyAutoGUI: A library for programmatically controlling the mouse and keyboard.
OpenCV: A library primarily aimed at real-time computer vision, also useful for image processing.

Game Development
Pygame: A set of Python modules designed for writing video games, including functionality for creating windows, handling user input, and displaying images and sounds.
Pyglet: A cross-platform windowing and multimedia library for Python, intended for developing games and other visually rich applications.

Cybersecurity
Paramiko: A library for making SSH2 connections (client and server) in Python, focusing on secure cryptographic operations.
Scapy: A powerful Python-based interactive packet manipulation tool and library.
Cryptography: A package to help you encrypt and decrypt data, manage keys, and implement various encryption algorithms.

Graphical User Interface (GUI)
Tkinter: The standard Python interface to the Tk GUI toolkit, commonly used for developing simple desktop applications.
PyQt/PySide: Bindings for the Qt application framework, providing tools to create sophisticated desktop applications.
Kivy: An open-source Python library for developing multitouch applications.

Networking:
Socket: A low-level networking interface for communicating over network protocols.
Twisted: An event-driven networking engine written in Python for building high-performance networking applications.

Cloud & DevOps
Boto3: The Amazon Web Services (AWS) SDK for Python, enabling Python developers to write software that makes use of Amazon services.
Ansible: An open-source automation tool, or platform, used for IT tasks such as configuration management, 
application deployment, and intra-service orchestration.
Fabric: A high-level Python library designed to execute shell commands remotely over SSH.
"""

# The collections library offers specialized container datatypes.

from collections import Counter

# Count the frequency of elements in a list
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
word_count = Counter(words)
print(f"Word frequency: {word_count}")

# Get the most common elements
most_common = word_count.most_common(2)
print(f"Two most common words: {most_common}")