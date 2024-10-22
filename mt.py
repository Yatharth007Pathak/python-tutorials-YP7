# Plotting a Basic Bar Plot:

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a bar plot
sns.barplot(x="day", y="total_bill", data=tips)

# Adding a title
plt.title('Average Total Bill by Day')

# Displaying the plot
plt.show()