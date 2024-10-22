# Plotting a Pair Plot:

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a pair plot
sns.pairplot(tips)

# Displaying the plot
plt.show()
