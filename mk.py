# Plotting a Scatter Plot:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Creating a scatter plot
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')

# Displaying the plot
plt.show()