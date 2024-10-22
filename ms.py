# Plotting a Basic Scatter Plot:

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Adding a title
plt.title('Scatter Plot of Total Bill vs Tip')

# Displaying the plot
plt.show()