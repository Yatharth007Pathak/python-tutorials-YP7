"""
Commonly Used Plots in matplotlib:
Line Plot: plt.plot(x, y)
Scatter Plot: plt.scatter(x, y)
Bar Plot: plt.bar(x, height)
Histogram: plt.hist(data, bins)
Pie Chart: plt.pie(sizes, labels=labels)

Customization Options in matplotlib:
Titles and Labels: plt.title(), plt.xlabel(), plt.ylabel()
Legend: plt.legend()
Grid: plt.grid()
Colors and Markers: plt.plot(x, y, color='red', marker='x')
Axes Limits: plt.xlim(), plt.ylim()
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data for plotting
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='b')

# Set the title and labels
ax.set_title('Simple Line Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# Show the plot
plt.show()
