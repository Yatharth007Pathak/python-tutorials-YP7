# Interpolation

from scipy.interpolate import interp1d
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Linear interpolation
linear_interp = interp1d(x, y)

# Create new x values
x_new = np.linspace(0, 4, 50)
y_new = linear_interp(x_new)

# Plot the results
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Interpolated line')
plt.legend()
plt.show()
