# Plotting Multiple Lines:

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Creating multiple line plots
plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x')

# Adding labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Line Plot')
plt.legend()

# Displaying the plot
plt.show()
