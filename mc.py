"""
The pandas library in Python is a powerful and flexible tool for data manipulation and analysis. 
It provides two main data structures: Series and DataFrame, which are essential for handling and analyzing structured data.

Key Features of pandas:
Data Structures:
Series: A one-dimensional labeled array that can hold any data type (integers, strings, floating-point numbers, etc.). 
It's similar to a list or a column in a table.
DataFrame: A two-dimensional labeled data structure with columns of potentially different types. It's similar to a spreadsheet or SQL table.
Data Manipulation: pandas provides a wide array of functions for data manipulation, including sorting, 
filtering, merging, reshaping, and aggregating data.
Data Cleaning: It offers functions to handle missing data, duplicate data, and to perform data type conversions.
Data Input/Output: pandas can read from and write to various file formats, including CSV, Excel, SQL databases, and JSON.
Time Series: It includes powerful tools for working with time series data.
"""

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Display the DataFrame
print(df)
