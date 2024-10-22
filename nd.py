# Fourier Transform


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.fft import fft

# Sample data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + 0.5 * np.sin(5 * x)

# Perform Fourier transform
yf = fft(y)
xf = np.fft.fftfreq(len(x), (x[1] - x[0]))

# Plotting the result
plt.plot(xf, np.abs(yf))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Fourier Transform')
plt.show()