"""
Customization Options in seaborn library:

Themes: We can set different themes using sns.set_theme() or sns.set_style() with options like 
'darkgrid', 'whitegrid', 'dark', 'white', and 'ticks'.
sns.set_theme(style='whitegrid')

Color Palettes: You can customize the color palette using sns.set_palette() or directly in the plotting functions.
sns.set_palette('husl')
"""

# Visualizing the Tips Dataset with Themes and Color Palettes

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Set a theme
sns.set_theme(style='darkgrid')

# Set a color palette
sns.set_palette('pastel')

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', hue='day', style='time', size='size', data=tips)

# Add titles and labels
plt.title('Scatter Plot of Tips Dataset')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')

# Display the plot
plt.show()

# Change the theme and palette and create another plot
sns.set_theme(style='whitegrid')
sns.set_palette('husl')

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', hue='time', data=tips)

# Add titles and labels
plt.title('Box Plot of Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')

# Display the plot
plt.show()
