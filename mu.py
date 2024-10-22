# Plotting a Basic Histogram:

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a histogram
sns.histplot(tips['total_bill'], bins=10, kde=True)

# Adding a title
plt.title('Histogram of Total Bill')

# Displaying the plot
plt.show()