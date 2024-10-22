"""
seaborn is a powerful Python data visualization library built on top of matplotlib. 
It provides a high-level interface for creating visually appealing and informative statistical graphics. 
seaborn is particularly useful for exploring and understanding data through visual patterns.

Key Features of seaborn:
Enhanced Aesthetics: seaborn automatically styles plots with a more modern, clean look than matplotlib.
Built-in Themes: It comes with several themes and color palettes that make it easy to create attractive visualizations.
Statistical Plots: seaborn provides functions to create complex statistical plots such as violin plots, box plots, and pair plots with minimal effort.
Integration with pandas: It works seamlessly with pandas DataFrames, making it easy to visualize data directly from a DataFrame.
"""

import matplotlib
matplotlib.use('TkAgg')  # Or another backend like 'Qt5Agg', etc.
import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in dataset
tips = sns.load_dataset('tips')

# Create a simple scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)

# Display the plot
plt.show()