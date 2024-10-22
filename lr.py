"""
statistics module

Measures of Central Tendency:
statistics.mean(data): Returns the arithmetic mean (average) of the data.
statistics.median(data): Returns the median (middle value) of the data.
statistics.mode(data): Returns the mode (most common value) of the data.

Measures of Dispersion:
statistics.stdev(data, xbar=None): Returns the standard deviation of the data. If xbar is provided, it is used as the mean (for efficiency).
statistics.variance(data, xbar=None): Returns the variance of the data. If xbar is provided, it is used as the mean.

Additional Functions:
statistics.pstdev(data, mu=None): Returns the population standard deviation.
statistics.pvariance(data, mu=None): Returns the population variance.
statistics.quantiles(data, n=4, method='exclusive'): Returns the quantiles of the data.
statistics.correlation(x, y): Returns the Pearson correlation coefficient between two data sets.

Classes:
statistics.NormalDist(mu=0, sigma=1): Represents a normal distribution and provides methods to calculate probabilities and quantiles.
"""

import statistics

# Sample data
data = [10, 20, 30, 40, 50]

# Measures of Central Tendency
mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode([1, 1, 2, 2, 3, 3, 4])

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

# Measures of Dispersion
stdev_value = statistics.stdev(data)
variance_value = statistics.variance(data)

print(f"Standard Deviation: {stdev_value}")
print(f"Variance: {variance_value}")

# Population statistics
population_data = [1, 2, 3, 4, 5]
pstdev_value = statistics.pstdev(population_data)
pvariance_value = statistics.pvariance(population_data)

print(f"Population Standard Deviation: {pstdev_value}")
print(f"Population Variance: {pvariance_value}")

# Quantiles
quantiles = statistics.quantiles(data, n=4)
print(f"Quartiles: {quantiles}")

# Correlation (requires two lists of data)
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
correlation = statistics.correlation(x, y)
print(f"Correlation: {correlation}")

# Normal Distribution
normal_dist = statistics.NormalDist(mu=0, sigma=1)
print(f"CDF at 0: {normal_dist.cdf(0)}")
print(f"PDF at 0: {normal_dist.pdf(0)}")
print(f"Quantile at 0.5: {normal_dist.inv_cdf(0.5)}")
