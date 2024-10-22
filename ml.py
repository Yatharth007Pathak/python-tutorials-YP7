# Plotting a Histogram:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Data for plotting
data = [22, 55, 62, 45, 21, 23, 41, 52, 48, 33, 29, 38, 31, 35]

# Creating a histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Simple Histogram')

# Displaying the plot
plt.show()