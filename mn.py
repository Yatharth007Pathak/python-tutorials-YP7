# Plotting a Pie Chart:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Data for plotting
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Creating a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Adding a title
plt.title('Simple Pie Chart')

# Displaying the chart
plt.show()