# Plotting a Box Plot:

import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a box plot
sns.boxplot(x="day", y="total_bill", data=tips)

# Adding a title
plt.title('Box Plot of Total Bill by Day')

# Displaying the plot
plt.show()