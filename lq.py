"""
The statistics module in Python provides functions for statistical operations and calculations. 
It includes functions for calculating measures of central tendency, dispersion, and distribution.

Common Functions and Classes

Measures of Central Tendency:
statistics.mean(data): Computes the average of the numbers in data.
statistics.median(data): Finds the middle value of data when sorted.
statistics.mode(data): Finds the most frequently occurring value in data. Handled with exception in case of no unique mode.

Measures of Dispersion:
statistics.stdev(data): Computes the sample standard deviation.
statistics.variance(data): Computes the sample variance.

Population Statistics:
statistics.pstdev(population_data): Computes the population standard deviation.
statistics.pvariance(population_data): Computes the population variance.

Quantiles:
statistics.quantiles(data, n): Computes the quantiles of data. In this example, n=4 for quartiles.

Correlation:
statistics.correlation(x, y): Computes the Pearson correlation coefficient. 
This function may not be available in all versions of the statistics module.

Normal Distribution:
statistics.NormalDist(mu=0, sigma=1): Represents a normal distribution with mean mu and standard deviation sigma. Methods:
cdf(x): Computes the cumulative distribution function.
pdf(x): Computes the probability density function.
inv_cdf(p): Computes the inverse cumulative distribution function (quantile).
"""

import statistics

# Sample data
data = [10, 20, 30, 40, 50]
more_data = [1, 1, 2, 2, 3, 3, 4]
population_data = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Measures of Central Tendency
mean_value = statistics.mean(data)
median_value = statistics.median(data)
try:
    mode_value = statistics.mode(more_data)
except statistics.StatisticsError as e:
    mode_value = e  # Handling mode error if there is no unique mode

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

# Measures of Dispersion
stdev_value = statistics.stdev(data)
variance_value = statistics.variance(data)

print(f"Standard Deviation: {stdev_value}")
print(f"Variance: {variance_value}")

# Population statistics
pstdev_value = statistics.pstdev(population_data)
pvariance_value = statistics.pvariance(population_data)

print(f"Population Standard Deviation: {pstdev_value}")
print(f"Population Variance: {pvariance_value}")

# Quantiles
quantiles = statistics.quantiles(data, n=4)  # Quartiles
print(f"Quartiles: {quantiles}")

# Correlation
try:
    correlation = statistics.correlation(x, y)
except AttributeError as e:
    correlation = "Correlation function is not available in this version of statistics module."

print(f"Correlation: {correlation}")

# Normal Distribution
try:
    normal_dist = statistics.NormalDist(mu=0, sigma=1)
    cdf_value = normal_dist.cdf(0)
    pdf_value = normal_dist.pdf(0)
    quantile_value = normal_dist.inv_cdf(0.5)
except AttributeError as e:
    cdf_value = pdf_value = quantile_value = "NormalDist is not available in this version of statistics module."

print(f"CDF at 0: {cdf_value}")
print(f"PDF at 0: {pdf_value}")
print(f"Quantile at 0.5: {quantile_value}")
