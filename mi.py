# Plotting a Line Graph:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creating a line plot
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Displaying the plot
plt.show()