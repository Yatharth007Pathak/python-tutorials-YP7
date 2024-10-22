"""
Commonly Used Plots in seaborn library:

Scatter Plot: sns.scatterplot(x, y, data)
Line Plot: sns.lineplot(x, y, data)
Bar Plot: sns.barplot(x, y, data)
Histogram: sns.histplot(data, bins)
Box Plot: sns.boxplot(x, y, data)
Violin Plot: sns.violinplot(x, y, data)
Heatmap: sns.heatmap(data, annot=True)
"""

# A pair plot is a powerful way to visualize pairwise relationships in a dataset.

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset
iris = sns.load_dataset('iris')

# Create a pair plot
sns.pairplot(iris, hue='species')

# Display the plot
plt.show()