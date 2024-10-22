"""
matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
It is widely used for plotting data and producing various types of graphs and charts.

Key Features of matplotlib:
Versatile Plotting: Allows you to create line plots, scatter plots, bar plots, histograms, and more.
Customization: Provides extensive options to customize plots, including colors, labels, scales, and styles.
Interactive Plots: Supports interactive features such as zooming and panning.
Integration: Works well with other libraries like numpy and pandas for data visualization.
"""

'''
TkAgg is a backend for Matplotlib that allows it to render plots using the Tkinter library, which is a standard GUI toolkit for Python. 
In Matplotlib, a "backend" refers to the layer that handles the rendering of plots and the interaction with the GUI or other output devices.

Here's a breakdown:
TkAgg:
Tk refers to Tkinter, a popular GUI library in Python used for creating windows, dialogs, and other graphical elements.
Agg refers to the Anti-Grain Geometry engine, a high-performance rendering engine used by Matplotlib to create high-quality plots.

Why Use TkAgg?
Cross-Platform: Tkinter is cross-platform, meaning that it works on Windows, macOS, and Linux, making TkAgg a versatile choice.
Interactive Plots: With TkAgg, we can create interactive plots that allow for zooming, panning, and updating in real-time, 
which is useful for dynamic data visualization.
Fallback Option: If the default backend isn't working (e.g., due to missing dependencies), 
TkAgg often serves as a reliable alternative because Tkinter is usually bundled with Python installations.
'''

import matplotlib
matplotlib.use('TkAgg')  # Or another backend like 'Agg', 'Qt5Agg', etc
import matplotlib.pyplot as plt

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plotting on the first subplot
ax1.plot([1, 2, 3], [4, 5, 6], 'r-')
ax1.set_title('First Plot')

# Plotting on the second subplot
ax2.bar(['A', 'B', 'C'], [3, 7, 2])
ax2.set_title('Second Plot')

# Displaying the plots
plt.tight_layout()
plt.show()