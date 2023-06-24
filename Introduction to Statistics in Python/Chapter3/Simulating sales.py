from scipy.stats import norm
import matplotlib.pyplot as plt

# Calculate new average amount
new_mean = 5000 * 1.2

# Calculate new standard deviation
new_sd = 2000 * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean,new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()