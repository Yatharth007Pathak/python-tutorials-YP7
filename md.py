"""
Commonly Used Functions in pandas library:
DataFrame Creation: pd.DataFrame(), pd.Series()
Reading/Writing Data: pd.read_csv(), pd.read_excel(), df.to_csv(), df.to_excel()
Data Selection: df.loc[], df.iloc[], df['column']
Data Manipulation: df.drop(), df.rename(), df.groupby(), df.merge(), df.pivot_table()
Handling Missing Data: df.isna(), df.dropna(), df.fillna()
Descriptive Statistics: df.describe(), df.mean(), df.median()
"""

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Accessing a column
print("\nName column:")
print(df['Name'])

# Filtering rows
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with Salary column:")
print(df)

# Reading from a CSV file
# Note: The 'file.csv' should exist in the same directory or provide an appropriate path.
try:
    df_from_csv = pd.read_csv('file.csv')
    print("\nDataFrame from CSV file:")
    print(df_from_csv)
except FileNotFoundError:
    print("\n'file.csv' not found.")

# Writing to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame has been written to 'output.csv'.")
