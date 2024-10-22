# Plotting a Bar Chart:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data for plotting
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]

# Creating a bar chart
plt.bar(categories, values)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')

# Displaying the chart
plt.show()