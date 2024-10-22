# Statistics

from scipy import stats
import numpy as np

# Descriptive statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = np.mean(data)
std_dev = np.std(data)
median = np.median(data)

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Median:", median)

# Probability distribution
normal_dist = stats.norm(loc=0, scale=1)
print("Probability of x=1:", normal_dist.pdf(1))